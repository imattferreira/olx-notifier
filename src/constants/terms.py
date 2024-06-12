from entities.term import Term

__appleWatchTerm = Term(
    term="apple watch",
    localization="municipal",
    min=800,
    max=1800,
    nosy_terms=[
        "series 6",
        "série 6",
        "series 5",
        "série 5",
        "series 4",
        "série 4",
        "series 3",
        "série 3",
        "series 2",
        "série 2",
        "series 1",
        "série 1",
    ]
)

__appleWatchTerm.set_price_range_by_term(term="SE", min=80, max=1200)

TERMS = [__appleWatchTerm]
