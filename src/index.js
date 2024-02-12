import notify from "./lib/notify.js";
import scrape from "./lib/scrape.js";
import { getAdsByTerm, saveAdsByTerm } from "./lib/store.js";

import TERMS from "./constants/terms.js";
import LOCALIZATIONS from "./constants/localizations.js";

function mountUrl({ term, localization, page }) {
  let baseUrl = "https://www.olx.com.br";

  baseUrl += LOCALIZATIONS[localization];
  baseUrl += `?q=${term}`;

  if (page && page > 1) {
    baseUrl += `&o=${page}`;
  }

  return baseUrl;
}

function mountScrape({ term, localization, page }) {
  return () => scrape(mountUrl({ term, localization, page }));
}

function mountScrapes({ totalOfPages, term, localization }) {
  if (totalOfPages === 0) {
    return [];
  }

  const offset = 2;
  const count = totalOfPages === 1 ? totalOfPages : totalOfPages - offset;
  const arr = Array(count);

  return arr.map((_, i) =>
    mountScrape({ localization, page: i + offset, term })
  );
}

function formatAd(ad) {
  return {
    locationDetails: ad.locationDetails,
    price: ad.price,
    thumbnail: ad.thumbnail,
    title: ad.title,
    url: ad.url,
  };
}

function isNotAdvertising(ad) {
  return ad.title !== undefined;
}

// TODO
function isInLineWithPreferences(filters) {
  return (ad) => {
    return ad;
  };
}

function isNewAd(stored) {
  return (ad) => {
    if (!stored) {
      return ad;
    }

    return stored.some((a) => a.url === ad.url);
  };
}

async function main() {
  for (const { filters, localization, term } of TERMS) {
    const serverData = await scrape(mountUrl({ term, localization, page: 1 }));

    const { pageIndex, pageSize, totalOfAds } = serverData.props.pageProps;
    const totalOfPages = Math.ceil(totalOfAds / pageSize) - pageIndex;

    const scraped = await Promise.all(
      mountScrapes({ localization, term, totalOfPages })
    );
    const lastNotifiedAds = await getAdsByTerm(term);

    const ads = scraped
      .concat(serverData)
      .flatMap((server) => server.props.pageProps.ads.map(formatAd))
      .filter(isNotAdvertising)
      .filter(isInLineWithPreferences(filters))
      .filter(isNewAd(lastNotifiedAds));

    await saveAdsByTerm(term, ads);

    for (const ad of ads) {
      // TODO add price, adjust icon
      await notify({
        icon: ad.thumbnail,
        link: ad.url,
        message: ad.title,
        title: `New offer for ${term}`,
      });
    }
  }
}

main();
