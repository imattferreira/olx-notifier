const TERMS = [
  {
    term: "apple watch",
    localization: "municipal", // municipal or region or state
    filters: {
      conditionalsByIntermediaryTerm: [
        {
          term: "SE",
          value: {
            min: 800,
            max: 1200,
          },
        },
      ],
      exclude: [
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
      ],
      value: {
        min: 800,
        max: 1800,
      },
    },
  },
];

export default TERMS;
