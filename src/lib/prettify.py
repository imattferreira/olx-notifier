from entities.ad import Ad
from entities.term import Term
from store import get_ads_by_term

def _is_new_ad(stored: list[dict]):
  def find_ad(ad: Ad) -> bool:
    if len(stored) == 0:
      return True

    matched = next((a for a in stored if a["url"] == ad.get_url()), None)

    return bool(matched)

    return find_ad;

def _is_not_advertising(ad: dict) -> bool:
  return ad["title"] != None

def _only_ads(data: list[dict]) -> list[dict]:
  flatted = list()

  for d in data:
    flatted.append(d["props"]["pageProps"]["ads"])

  return flatted

def fn_reduce(initial_data: any, fns: list) -> any:
  tmp = initial_data

  for fn in fns:
    tmp = fn(tmp)

  return tmp

# TODO:
def _only_preferences(filters: list[dict]):
  def is_according_with_prefs(ad) -> bool:
    return bool(ad)

# TODO: change way to filter ads
def prettify(ads: list[dict], term: Term) -> list[Ad]:
  last_notified_ads = get_ads_by_term(term.term)

  return fn_reduce(
    ads,
    (
      Ad.parse,
      _only_ads, 
      _is_not_advertising,
      _only_preferences(filters),
      _is_new_ad(last_notified_ads)
    )
  )
