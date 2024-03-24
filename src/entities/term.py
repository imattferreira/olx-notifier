class Term:
  term: str
  localization: str
  nosy_terms = []
  price_range = {
    min: int,
    max: int
  }
  price_range_by_term = []

  def __init__(self, term: str):
    self.term = term

  def set_localization(self, localization: str) -> None:
    self.localization = localization

  def set_nosy_term(self, term: str) -> None:
    self.nosy_terms.append(term)

  def set_price_range(self, min: int, max: int) -> None:
    self.price_range["min"] = min
    self.price_range["max"] = max

  def set_price_range_by_term(self, term: str, min: int, max: int) -> None:
    filter = {
      term,
      min,
      max
    }

    self.price_range_by_term.append(filter)
