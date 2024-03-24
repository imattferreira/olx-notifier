import json
from typing import Union
from datetime import datetime
from entities.ad import Ad

def _get_store() -> list[dict]:
  database = open("src/database.json", "r")
  data = database.read()

  database.close()

  return json.loads(data)

def _save_store(store: list[dict]) -> None:
  database = open("src/database.json", "w")
  data = json.dumps(store)

  database.write(data)
  database.close()

def _find_term(term: str, stored: list[dict]) -> Union[list[dict], None]:
  return next((i for i in stored if i["term"] == term), False)

def get_ads_by_term(term: str) -> Union[list[dict], None]:
  stored = _get_store()

  stored_ads_by_term = _find_term(term, stored)

  if not stored_ads_by_term:
    return None
  
  return stored_ads_by_term["ads"]

def save_ads_by_term(term: str, ads: list[Ad]) -> None:
  stored = _get_store()
  stored_ads_by_term = _find_term(term, stored)
  modified_at = datetime.now()

  if not isinstance(stored_ads_by_term, list):
    data = {
      term,
      ads,
      modified_at
    }

    stored.append(data)
  else:
    stored_ads_by_term["ads"] = ads
    stored_ads_by_term["modified_at"] = modified_at

  _save_store(stored)
  