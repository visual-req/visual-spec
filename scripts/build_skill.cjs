const { spawnSync } = require("node:child_process");
const fs = require("node:fs");
const path = require("node:path");

function getRepoRoot() {
  return path.resolve(__dirname, "..");
}

function readPackageJson(repoRoot) {
  const packageJsonPath = path.join(repoRoot, "package.json");
  return JSON.parse(fs.readFileSync(packageJsonPath, "utf-8"));
}

function ensureDir(dirPath) {
  fs.mkdirSync(dirPath, { recursive: true });
}

function main() {
  const repoRoot = getRepoRoot();
  const pkg = readPackageJson(repoRoot);

  const skillDir = path.join(repoRoot, "skills", "visual-spec-skill");
  if (!fs.existsSync(skillDir)) {
    throw new Error(`Skill dir not found: ${skillDir}`);
  }

  const distDir = path.join(repoRoot, "dist");
  ensureDir(distDir);

  const version = pkg.version || "0.0.0";
  const outputPath = path.join(distDir, `visual-spec-skill-${version}.skill`);

  if (fs.existsSync(outputPath)) {
    fs.rmSync(outputPath);
  }

  const result = spawnSync(
    "zip",
    ["-r", outputPath, ".", "-x", "*.DS_Store", "-x", "*/.DS_Store"],
    { cwd: skillDir, stdio: "inherit" }
  );

  if (result.error) {
    throw new Error(
      `Failed to run 'zip'. Please ensure 'zip' is installed and available in PATH. ${result.error.message}`
    );
  }

  if (result.status !== 0) {
    process.exit(result.status);
  }

  process.stdout.write(`${outputPath}\n`);
}

main();

