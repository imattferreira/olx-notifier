from typing import Union, Literal


class Term:
    term: str
    localization: Literal["municipal", "region", "state"]
    nosy_terms: list[str] = []
    price_range: dict[str, int] = {"min": 0, "max": 0}
    price_range_by_term: list[dict[str, Union[str, int]]] = []

    def __init__(
        self,
        term: str,
        localization: Literal["municipal", "region", "state"],
        min: int,
        max: int,
        nosy_terms: list[str]
    ):
        self.term = term
        self.localization = localization
        self.price_range["min"] = min
        self.price_range["max"] = max
        self.nosy_terms = nosy_terms

    def set_price_range_by_term(self, term: str, min: int, max: int) -> None:
        filter: dict[str, Union[str, int]] = {
            "term": term,
            "min": min,
            "max": max
        }

        self.price_range_by_term.append(filter)
