import LOCALIZATIONS from "../constants/localizations.js";

const START_SCRIPT_TAG = '<script id="__NEXT_DATA__" type="application/json">';
const END_SCRIPT_TAG = "</script>";

function mountUrl({ term, localization, page }) {
  let baseUrl = "https://www.olx.com.br";

  baseUrl += LOCALIZATIONS[localization];
  baseUrl += `?q=${term}`;

  if (page && page > 1) {
    baseUrl += `&o=${page}`;
  }

  return baseUrl;
}

async function scrape({ term, localization, page }) {
  const url = mountUrl({ term, localization, page });

  const request = await fetch(url);
  const text = await request.text();

  const startIndex = text.indexOf(START_SCRIPT_TAG);
  const endIndex = text.lastIndexOf(END_SCRIPT_TAG);
  // TODO remove replaces
  const json = text
    .slice(startIndex, endIndex)
    .replace('<script id="__NEXT_DATA__" type="application/json">', "")
    .replace("</script>", "");

  return JSON.parse(json);
}

export default scrape;
