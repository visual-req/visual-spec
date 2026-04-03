const fs = require("node:fs/promises");
const path = require("node:path");

function parseArgs(argv) {
  const args = new Set(argv);
  const getValue = (name) => {
    const index = argv.indexOf(name);
    if (index === -1) return undefined;
    return argv[index + 1];
  };
  return {
    dryRun: args.has("--dry-run"),
    force: args.has("--force"),
    target: getValue("--target"),
    skillDir: getValue("--skill-dir") || getValue("--target-skill-dir"),
    skillsDir: getValue("--skills-dir") || getValue("--target-skills-dir"),
  };
}

async function pathExists(filePath) {
  try {
    await fs.stat(filePath);
    return true;
  } catch {
    return false;
  }
}

async function removeDirRecursive(dirPath) {
  const stat = await fs.lstat(dirPath);
  if (!stat.isDirectory()) {
    await fs.unlink(dirPath);
    return;
  }

  const entries = await fs.readdir(dirPath);
  await Promise.all(
    entries.map(async (entry) => {
      const entryPath = path.join(dirPath, entry);
      await removeDirRecursive(entryPath);
    }),
  );

  await fs.rmdir(dirPath);
}

async function copyDirRecursive(fromDir, toDir) {
  await fs.mkdir(toDir, { recursive: true });
  const entries = await fs.readdir(fromDir, { withFileTypes: true });

  await Promise.all(
    entries.map(async (entry) => {
      const fromPath = path.join(fromDir, entry.name);
      const toPath = path.join(toDir, entry.name);

      if (entry.isDirectory()) {
        await copyDirRecursive(fromPath, toPath);
        return;
      }

      if (entry.isSymbolicLink()) {
        const linkTarget = await fs.readlink(fromPath);
        try {
          await fs.unlink(toPath);
        } catch {}
        await fs.symlink(linkTarget, toPath);
        return;
      }

      await fs.copyFile(fromPath, toPath);
    }),
  );
}

async function main() {
  const { dryRun, force, target, skillDir, skillsDir } = parseArgs(process.argv.slice(2));

  const packageRoot = path.resolve(__dirname, "..");
  const sourceSkillDir = path.join(packageRoot, "skills", "visual-spec-skill");
  const initCwd = target || process.env.INIT_CWD || process.cwd();
  const resolvedSkillsDir =
    skillsDir && path.resolve(initCwd, skillsDir);
  const resolvedSkillDir =
    skillDir && path.resolve(initCwd, skillDir);
  const targetSkillDir =
    resolvedSkillDir ||
    (resolvedSkillsDir
      ? path.join(resolvedSkillsDir, "visual-spec-skill")
      : path.join(initCwd, ".trae", "skills", "visual-spec-skill"));

  if (!(await pathExists(sourceSkillDir))) {
    throw new Error(`Skill source directory not found: ${sourceSkillDir}`);
  }

  if (!force && path.resolve(initCwd) === packageRoot) {
    if (!dryRun) return;
  }

  const targetSkillsDir = path.dirname(targetSkillDir);

  if (dryRun) {
    process.stdout.write(
      [
        "[vspec] dry-run",
        `- source: ${sourceSkillDir}`,
        `- target: ${targetSkillDir}`,
      ].join("\n") + "\n",
    );
    return;
  }

  await fs.mkdir(targetSkillsDir, { recursive: true });

  const targetExists = await pathExists(targetSkillDir);
  if (targetExists && force) {
    await removeDirRecursive(targetSkillDir);
  }

  await copyDirRecursive(sourceSkillDir, targetSkillDir);
  process.stdout.write(`[vspec] installed to ${targetSkillDir}\n`);
}

main().catch((error) => {
  process.stderr.write(`[vspec] install failed: ${error?.message || error}\n`);
  process.exitCode = 1;
});
