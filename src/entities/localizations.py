from typing import Union

class Localizations:
  stored = {
    "state": "/estado-sp",
    "region": "/estado-sp/regiao-de-bauru-e-marilia",
    "municipal": "/estado-sp/regiao-de-bauru-e-marilia/bauru"
  }

  def get_localization(self, localization: str) -> Union[str, Exception]:
    item = self.stored.get(localization)

    if not item:
      raise Exception("[localization] not found")

    return item
