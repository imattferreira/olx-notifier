import json

class Ad:
  localization_details: any # TODO: adjust
  price: float
  thumbnail: str
  title: str
  url: str

  def __init__(
    self, 
    localization_details: any,
    price: float, 
    thumbnail: str, 
    title: str, 
    url: str
    ):
    self.localization_details = localization_details
    self.price = price
    self.thumbnail = thumbnail
    self.title = title
    self.url = url

  def get_localization_details(self) -> any:
    return self.localization_details

  def get_price(self) -> float:
    return self.price

  def get_thumbnail(self) -> str:
    return self.thumbnail

  def get_title(self) -> str:
    return self.title

  def get_url(self) -> str:
    return self.url

  def stringify(self) -> str:
    data = {
      localization_details: self.localization_details,
      price: self.price,
      thumbnail: self.thumbnail,
      title: self.title,
      url: self.url
    }

    return json.dumps(data)

  @staticmethod
  def parse(self, data: str) -> Ad:
    ad = json.loads(data)

    return Ad(
      localization_details=ad["locationDetails"],
      price=float(ad["price"]),
      thumbnail=ad["thumbnail"],
      title=ad["title"],
      url=ad["url"]
    )

  @staticmethod
  def parse(self, data: dict) -> Ad:
    return Ad(
      localization_details=data["locationDetails"],
      price=float(data["price"]),
      thumbnail=data["thumbnail"],
      title=data["title"],
      url=data["url"]
    )