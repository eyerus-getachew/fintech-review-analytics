from sqlalchemy import create_engine
import pandas as pd


# PostgreSQL connection
engine = create_engine(
    "postgresql://postgres:1901@localhost:5432/bank_reviews"
)


# Load dataset
df = pd.read_csv(
    "data/raw/task2_sentiment_analysis.csv"
)


# Create banks dataframe
banks_df = pd.DataFrame({
    "bank_name": [
        "Commercial Bank of Ethiopia",
        "Bank of Abyssinia",
        "Dashen Bank"
    ],

    "app_name": [
        "CBE Mobile Banking",
        "BOA Mobile Banking",
        "Dashen Super App"
    ]
})


# Insert banks data
banks_df.to_sql(
    "banks",
    engine,
    if_exists="append",
    index=False
)

print("Banks data inserted successfully!")


# Map bank names to IDs
bank_mapping = {
    "CBE": 1,
    "BOA": 2,
    "Dashen": 3
}


# Load original cleaned dataset
original_df = pd.read_csv(
    "data/raw/fintech_reviews_clean.csv"
)


# Add bank_id
df["bank_id"] = original_df["bank"].map(bank_mapping)


# Add additional columns
df["rating"] = original_df["rating"]
df["review_date"] = original_df["date"]
df["source"] = original_df["source"]


# Rename columns
df.rename(columns={
    "review": "review_text"
}, inplace=True)


# Select final columns
reviews_df = df[
    [
        "bank_id",
        "review_text",
        "rating",
        "review_date",
        "sentiment_label",
        "sentiment_score",
        "identified_theme",
        "source"
    ]
]


# Insert reviews data
reviews_df.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)

print("Reviews data inserted successfully!")