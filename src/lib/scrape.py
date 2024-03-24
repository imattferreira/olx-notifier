from typing import Union
import requests
import json

# OLX hasn't migrated to Next.JS AppRouter yet, so we can use it in our favor
START_SCRIPT_TAG = '<script id="__NEXT_DATA__" type="application/json">'
END_SCRIPT_TAG = "</script>"

def _mount_url(term: str, localization: str, page: int) -> str:
  base_url = "https://olx.com.br"

  base_url += LOCALIZATIONS.get(localization)
  base_url += f"?q={term}"

  if page and page > 1:
    base_url += f"&o={page}"

  return base_url

def _extract_server_data(html: str) -> dict:
  start_index = html.index(START_SCRIPT_TAG)
  end_index = html.index(END_SCRIPT_TAG)

  data = html[start_index:end_index].replace(START_SCRIPT_TAG, "").replace(END_SCRIPT_TAG, "")

  return json.loads(data)["props"]["pageProps"]

def scrape(term: str, localization: str, page: int) -> Union[dict, Exception]:
  url = _mount_url(term, localization, page)

  response = requests.get(url)

  if response.status_code != 200:
    raise Exception("scraping failed!")
  
  return _extract_server_data(response.text)