# OlX Notifier

OLX Notifier is a study project that helps your creator (also known as me, @imattferreira) to be notified about the newest ads about specific terms and filters.

In my personal computer, this script was configured to run every 12:00 PM, notifying about the newest ADs that fit with pre-configured filters, like region, price and terms to be ignored.

## Requirements

- `Python > 3.x`
- `Homebrew > 4.x`

## Getting Started

- Create your virtual-env inside the root folder of project `python3 -m venv .venv`
- Load your virtual env `source ./.venv/bin/activate`
- Install deps `pip install -r ./requirements.txt`
- Go to `./src/constants/terms.py` and configure the terms that you want to be notified of, configuring the term to be searched, the price range, terms to be ignored and the price range of specific terms
- Run apps `python3 ./src/main.py`
