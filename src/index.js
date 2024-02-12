import notify from "./lib/notify.js";
import scrape from "./lib/scrape.js";
import prettify from "./lib/prettify.js";
import { saveAdsByTerm } from "./lib/store.js";

import TERMS from "./constants/terms.js";

function mountConcurrentScrape({ term, localization, page }) {
  return () => scrape({ term, localization, page });
}

function concurrentScrapes({ totalOfPages, term, localization }) {
  if (totalOfPages === 0) {
    return [];
  }

  const offset = 2;
  const count = totalOfPages === 1 ? totalOfPages : totalOfPages - offset;
  const arr = Array(count);

  const promises = arr.map((_, i) =>
    mountConcurrentScrape({ localization, page: i + offset, term })
  );

  return Promise.all(promises);
}

async function main() {
  for (const { filters, localization, term } of TERMS) {
    const serverData = await scrape({ localization, page: 1, term });

    const { pageIndex, pageSize, totalOfAds } = serverData.props.pageProps;
    const totalOfPages = Math.ceil(totalOfAds / pageSize) - pageIndex;

    const scraped = await concurrentScrapes({
      localization,
      term,
      totalOfPages,
    });
    const ads = await prettify({
      ads: scraped.concat(serverData),
      term,
      filters,
    });

    await saveAdsByTerm(term, ads);

    for (const ad of ads) {
      await notify({
        icon: ad.thumbnail,
        link: ad.url,
        message: ad.title,
        price: ad.price,
        title: `New offer for ${term}`,
      });
    }
  }
}

main();
