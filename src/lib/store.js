import fs from "node:fs";

const databasePathname = new URL("../database.json", import.meta.url).pathname;

async function getStore() {
  const content = await fs.promises.readFile(databasePathname);

  return JSON.parse(content.toString()).data;
}

async function saveStore(data) {
  await fs.promises.writeFile(databasePathname, data);
}

function findTerm(term, store) {
  return store.find((t) => t.term === term);
}

export async function getAdsByTerm(term) {
  const store = await getStore();
  const storedTerm = findTerm(term, store);

  if (!storedTerm) {
    return null;
  }

  return storedTerm.ads;
}

export async function saveAdsByTerm(term, ads) {
  const store = await getStore();
  const storedTerm = findTerm(term, store);

  if (storedTerm) {
    storedTerm.ads = ads;
    storedTerm.modifiedAt = Date.now();
  } else {
    store.push({ term, ads, modifiedAt: Date.now() });
  }

  const updatedStore = JSON.stringify({ data: store });

  await saveStore(updatedStore);
}
