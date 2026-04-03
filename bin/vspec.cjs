#!/usr/bin/env node

const { spawnSync } = require("node:child_process");
const path = require("node:path");

function main() {
  const scriptPath = path.resolve(__dirname, "..", "scripts", "postinstall.cjs");
  const args = process.argv.slice(2);

  const result = spawnSync(process.execPath, [scriptPath, ...args], {
    stdio: "inherit",
    env: process.env,
  });

  process.exit(result.status ?? 0);
}

main();
