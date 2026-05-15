from google_play_scraper import reviews_all
import pandas as pd


apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}


all_reviews = []


for bank, app_id in apps.items():

    print(f"Scraping reviews for {bank}...")

    reviews = reviews_all(
        app_id,
        sleep_milliseconds=0,
        lang='en',
        country='et'
    )

    for review in reviews:

        all_reviews.append({
            "review": review.get("content"),
            "rating": review.get("score"),
            "date": review.get("at"),
            "bank": bank,
            "source": "Google Play"
        })


# Create DataFrame
df = pd.DataFrame(all_reviews)

print(f"\nInitial review count: {len(df)}")


# Remove duplicates
df.drop_duplicates(subset=["review"], inplace=True)

print(f"Review count after removing duplicates: {len(df)}")


# Remove missing values
before_missing = len(df)

df.dropna(subset=["review", "rating"], inplace=True)

after_missing = len(df)

print(f"Rows removed with missing values: {before_missing - after_missing}")


# Normalize dates
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")


# Keep required columns
df = df[["review", "rating", "date", "bank", "source"]]


# Save cleaned dataset
output_path = "data/raw/fintech_reviews_clean.csv"

df.to_csv(output_path, index=False)

print(f"\nClean dataset saved to: {output_path}")

print("\nFinal Dataset Preview:")
print(df.head())

print(f"\nFinal review count: {len(df)}")