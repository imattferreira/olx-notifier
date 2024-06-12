from typing import Any
from entities.ad import Ad
from entities.term import Term
from store import get_ads_by_term


def __flat(l: list[list[Any]]) -> list[Any]:
    return [x for xs in l for x in xs]


def __is_advertising(ad: dict[str, Any]) -> bool:
    return not "subject" in ad


def __is_preferable(ad: Ad, term: Term) -> bool:
    for nosy in term.nosy_terms:
        if nosy in ad.title:
            return False

    if ad.price < term.price_range["min"] or ad.price > term.price_range["max"]:
        return False

    for p in term.price_range_by_term:
        if str(p["term"]) not in ad.title:
            continue

        if ad.price < int(p["min"]) or ad.price > int(p["max"]):
            return False

    return True


def __format(ads: list[dict[str, Any]]) -> list[Ad]:
    result: list[Ad] = []

    for ad in ads:
        if not __is_advertising(ad):
            result.append(Ad.parse(ad))

    return result


def __is_inside(ad: Ad, last_notified_ads: list[Ad]) -> bool:
    for notified_ad in last_notified_ads:
        if ad.url == notified_ad.url:
            return True

    return False


def __get_newest_ads(ads: list[Ad], term: Term) -> list[Ad]:
    result: list[Ad] = []
    last_notified_ads = get_ads_by_term(term.term)

    for ad in ads:
        if __is_preferable(ad, term) and not __is_inside(ad, last_notified_ads):
            result.append(ad)

    return result


def prettify(ads: list[list[dict[str, Any]]], term: Term):

    flatted = __flat(ads)
    formatted = __format(flatted)
    newest_ads = __get_newest_ads(formatted, term)

    return newest_ads
