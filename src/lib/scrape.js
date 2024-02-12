const START_SCRIPT_TAG = '<script id="__NEXT_DATA__" type="application/json">';
const END_SCRIPT_TAG = "</script>";

async function scrape(url) {
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
