from typing import Any
from constants.terms import TERMS
from lib.scrape import scrape
import math
from lib.prettify import prettify
from lib.store import save_ads_by_term
from lib.notify import notify


def main():
    for term in TERMS:
        server = scrape(term=term, page=1)
        ads: list[list[dict[str, Any]]] = []

        page_size = server["props"]["pageProps"]["pageSize"]
        ads_count = server["props"]["pageProps"]["totalOfAds"]

        pages_count = math.ceil(ads_count / page_size)
        ads.append(server["props"]["pageProps"]["ads"])

        if pages_count >= 2:
            for p in range(2, pages_count):
                d = scrape(term=term, page=p)
                ads.append(d["props"]["pageProps"]["ads"])

        prettified = prettify(ads=ads, term=term.term)

        save_ads_by_term(ads=prettified, term=term.term)
        notify(term=term.term, ads=prettified)


main()
