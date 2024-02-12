import { exec as execCb } from "node:child_process";
import { promisify } from "node:util";

const exec = promisify(execCb);

async function installDeps() {
  const { stderr } = await exec("brew install terminal-notifier");

  if (stderr) {
    throw new Error(stderr);
  }
}

async function hasNecessaryDeps() {
  const { stdout, stderr } = await exec("brew list | grep terminal-notifier");

  if (stderr) {
    throw new Error(stderr);
  }

  return !!stdout;
}

async function prepare() {
  const hasDeps = await hasNecessaryDeps();

  if (!hasDeps) {
    await installDeps();
  }
}

async function notify({ title, icon, message, link }) {
  try {
    const command = `terminal-notifier -message "${message}" -title "${title}" -open "${link}" -sound default`;

    await prepare();
    await exec(command);
  } catch {}
}

export default notify;
