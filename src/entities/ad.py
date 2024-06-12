from typing import Any
import json


def floated_brl(currency: str) -> float:
    cleaned = currency.replace("R$", "").replace(
        ".", "").replace(",", ".").strip()

    return float(cleaned)


class Ad:
    localization_details: dict[str, str]
    price: float
    thumbnail: str
    title: str
    url: str

    def __init__(
        self,
        localization_details: dict[str, str],
        price: float,
        thumbnail: str,
        title: str,
        url: str,
    ):
        self.localization_details = localization_details
        self.price = price
        self.thumbnail = thumbnail
        self.title = title
        self.url = url

    def stringify(self) -> str:
        data = {
            "localization_details": self.localization_details,
            "price": self.price,
            "thumbnail": self.thumbnail,
            "title": self.title,
            "url": self.url
        }

        return json.dumps(data)

    @staticmethod
    def parse(data: dict[str, Any]):
        return Ad(
            localization_details=data["locationDetails"],
            price=floated_brl(data["price"]),
            thumbnail=data["thumbnail"],
            title=data["title"],
            url=data["url"]
        )
