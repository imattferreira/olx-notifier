from typing import Any
from entities.ad import Ad
import json


def get_ads_by_term(term: str):
    with open("./src/database.json", "r") as file:
        result: list[Ad] = []
        data = json.loads(file.read())["data"]

        for i in data:
            if i["term"] == term:
                for j in i["ads"]:
                    result.append(Ad.parse(j))

        file.close()
        return result


def save_ads_by_term(term: str, ads: list[Ad]):
    with open("./src/database.json", "wr") as file:
        data = json.loads(file.read())["data"]
        updated: list[dict[str, Any]] = []

        for i in data:
            if i["term"] != term:
                updated.append(i)

        updated.append({"term": term, "ads": ads})
        file.write(json.dumps({"data": updated}))
        file.close()
