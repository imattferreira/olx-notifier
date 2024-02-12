import { getAdsByTerm } from "./store";

function formatAd(ad) {
  return {
    locationDetails: ad.locationDetails,
    price: ad.price,
    thumbnail: ad.thumbnail,
    title: ad.title,
    url: ad.url,
  };
}

function isNewAd(stored) {
  return (ad) => {
    if (!stored) {
      return ad;
    }

    return !stored.some((a) => a.url === ad.url);
  };
}

function isNotAdvertising(ad) {
  return ad.title !== undefined;
}

// TODO
function onlyPreferences(filters) {
  return (ad) => {
    return ad;
  };
}

async function prettify({ ads, term, filters }) {
  const lastNotifiedAds = await getAdsByTerm(term);

  return ads
    .flatMap((server) => server.props.pageProps.ads.map(formatAd))
    .filter(isNotAdvertising)
    .filter(onlyPreferences(filters))
    .filter(isNewAd(lastNotifiedAds));
}

export default prettify;
