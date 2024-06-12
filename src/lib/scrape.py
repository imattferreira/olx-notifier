from typing import Literal, Any
from entities.term import Term
import urllib.parse
import requests
import json

START_SCRIPT_TAG = "<script id=\"__NEXT_DATA__\" type=\"application/json\">"
END_SCRIPT_TAG = "</script>"

LOCALIZATIONS = {
    "municipal": "/estado-sp/regiao-de-bauru-e-marilia/bauru",
    "region": "/estado-sp/regiao-de-bauru-e-marilia",
    "state": "/estado-sp"
}


def mount_url(
    term: str,
    localization: Literal["municipal", "region", "state"],
    page: int
) -> str:
    url = "https://www.olx.com.br"
    encoded_term = urllib.parse.quote(term)

    url += LOCALIZATIONS[localization]
    url += f"?q={encoded_term}"

    if page > 1:
        url += f"&o={page}"

    return url


def scrape(term: Term, page: int) -> dict[str, Any]:
    url = mount_url(term=term.term, localization=term.localization, page=page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }

    res = requests.get(url=url, headers=headers)

    if not res.ok:
        raise Exception("scraping failed!")

    html = res.text

    start_index = html.index(START_SCRIPT_TAG)
    end_index = html.index(END_SCRIPT_TAG, start_index)
    slicer = slice(start_index, end_index)

    jj = html[slicer].replace(
        START_SCRIPT_TAG, "").replace(END_SCRIPT_TAG, "")

    return json.loads(jj)
