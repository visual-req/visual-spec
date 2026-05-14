#!/usr/bin/env node

const { spawnSync } = require("node:child_process");
const fs = require("node:fs");
const path = require("node:path");

function readPackageVersion() {
  try {
    const packageJsonPath = path.resolve(__dirname, "..", "package.json");
    const raw = fs.readFileSync(packageJsonPath, "utf8");
    const parsed = JSON.parse(raw);
    return typeof parsed.version === "string" ? parsed.version : undefined;
  } catch {
    return undefined;
  }
}

function printHelp() {
  const version = readPackageVersion();
  const header = version ? `vspec ${version}` : "vspec";
  process.stdout.write(
    [
      header,
      "",
      "Usage:",
      "  vspec [install] [--force] [--dry-run] [--target <dir>] [--skills-dir <dir> | --skill-dir <dir>]",
      "  vspec --version",
      "  vspec --help",
      "",
      "Commands:",
      "  install    Install the visual-spec skill into a target directory (default)",
      "",
      "Options:",
      "  --target <dir>     The project directory to install into (defaults to INIT_CWD or cwd)",
      "  --skills-dir <dir> Target skills directory (installs into <skills-dir>/visual-spec)",
      "  --skill-dir <dir>  Target skill directory (installs into <skill-dir>)",
      "  --force            Overwrite existing installation",
      "  --dry-run          Print resolved paths without writing files",
    ].join("\n") + "\n",
  );
}

function main() {
  const scriptPath = path.resolve(__dirname, "..", "scripts", "postinstall.cjs");
  const args = process.argv.slice(2);

  if (args.includes("--help") || args.includes("-h")) {
    printHelp();
    return;
  }
  if (args.includes("--version") || args.includes("-v")) {
    process.stdout.write(`${readPackageVersion() || "unknown"}\n`);
    return;
  }

  const normalizedArgs =
    args.length === 0 || args[0].startsWith("-") || args[0] === "install"
      ? args.filter((a) => a !== "install")
      : args;

  const result = spawnSync(process.execPath, [scriptPath, ...normalizedArgs], {
    stdio: "inherit",
    env: process.env,
  });

  process.exit(result.status ?? 0);
}

main();
