# TODO: parse ads when get from database store
# TODO: stringify ads before store in database
# TODO: validate all code
# TODO: apply filters in scraped ads

import math
from lib.notify import notify
from lib.prettify import prettify
from lib.scrape import scrape
from lib import store
from entities.localizations import Localizations
from entities.term import Term

def main(terms: list[Term]):
  for term in terms:
    data = scrape(term=term.term, localization=term.localization, page=1)

    page_index = data["pageIndex"]
    page_size = data["pageSize"]
    ads_count = data["totalOfAds"]

    pages_count = math.ceil(ads_count / page_size) - page_index
    data_scraped = list(data);

    if pages_count == 0:
      data_scraped.append([])
    else:
      offset = 2
      pages_to_scrape_count = pages_count if pages_count == 1  else pages_count - offset

      # TODO: make parallel requests of rest of pages


    ads = prettify(ads=data_scraped, term=term.term)

    store.save_ads_by_term(term, ads)

    for ad in ads:
      notify(
        icon=ad["icon"], 
        link=ad["link"], 
        message=f"{ad["price"]} - {ad["title"]}", 
        title=f"New offer for {term}"
      )