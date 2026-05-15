# Fintech Review Analytics

Customer Experience Analytics for Ethiopian Fintech Apps.

## Objective

This project analyzes Google Play Store reviews from Ethiopian banking applications to uncover customer sentiment, recurring complaints, and feature requests.

## Banks Included

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

## Technologies Used

- Python
- pandas
- google-play-scraper
- GitHub Actions
- pytest

## Data Collection

Reviews were scraped from the Google Play Store using the `google-play-scraper` Python package.

### Data Fields Collected

- Review text
- Rating
- Review date
- Bank name
- Source

### Collection Summary

- Total reviews collected: 11,495
- Final cleaned reviews: 8,328

## Preprocessing Steps

The following preprocessing steps were applied:

- Removed duplicate reviews
- Removed rows with missing review text or ratings
- Normalized dates to YYYY-MM-DD format
- Exported cleaned dataset as CSV

## Project Structure

- `scripts/` → scraping and preprocessing scripts
- `data/raw/` → raw datasets
- `notebooks/` → analysis notebooks
- `tests/` → unit tests

## Limitations

- Some reviews contain emojis or mixed languages
- Google Play review availability may change over time
- Duplicate reviews were common across apps