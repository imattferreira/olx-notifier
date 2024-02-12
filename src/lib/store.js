import fs from "node:fs";

const databasePathname = new URL("../database.json", import.meta.url).pathname;

export async function getAdsByTerm(term) {
  const content = await fs.promises.readFile(databasePathname);

  const stored = JSON.parse(content.toString()).data;
  const storedTerm = stored.find((t) => t.term === term);

  if (!storedTerm) {
    return null;
  }

  return storedTerm.ads;
}

export async function saveAdsByTerm(term, ads) {
  const content = await fs.promises.readFile(databasePathname);

  const stored = JSON.parse(content.toString()).data;
  const storedTerm = stored.find((t) => t.term === term);

  if (storedTerm) {
    storedTerm.ads = ads;
    storedTerm.modifiedAt = Date.now();
  } else {
    stored.push({ term, ads, modifiedAt: Date.now() });
  }

  await fs.promises.writeFile(databasePathname, JSON.stringify(stored));
}
