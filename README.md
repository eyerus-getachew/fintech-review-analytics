# Fintech Review Analytics

Customer Experience Analytics for Ethiopian Fintech Apps

---

# Project Overview

This project analyzes customer reviews collected from Ethiopian mobile banking applications on the Google Play Store. The goal is to transform unstructured customer feedback into actionable business insights using data engineering, natural language processing (NLP), sentiment analysis, thematic analysis, and PostgreSQL database integration.

The project was developed as a real-world analytics pipeline simulating how financial institutions and consulting firms can leverage customer feedback to improve mobile banking products, customer satisfaction, and retention strategies.

The analysis focuses on three Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

# Business Problem

Mobile banking adoption in Ethiopia continues to grow rapidly. Customers frequently leave reviews on the Google Play Store describing their experiences, frustrations, and feature requests.

These reviews contain valuable business intelligence such as:

- recurring technical issues
- app performance problems
- customer satisfaction indicators
- desired features
- usability concerns
- customer support complaints

Without systematic analysis, this information remains unstructured and difficult to use. This project builds a complete analytics workflow that converts raw reviews into structured insights for product and business teams.

---

# Project Objectives

The main objectives of this project are:

- Scrape customer reviews from the Google Play Store
- Clean and preprocess review data
- Perform sentiment analysis using NLP models
- Identify recurring themes and complaints
- Store processed data in PostgreSQL
- Generate business-focused insights and recommendations

---

# Dataset Information

Reviews were collected from the Google Play Store using the `google-play-scraper` Python library.

## Applications Included

| Bank | Application |
|---|---|
| Commercial Bank of Ethiopia | CBE Mobile Banking |
| Bank of Abyssinia | BOA Mobile Banking |
| Dashen Bank | Dashen Super App |

---

# Data Fields Collected

The following fields were collected during scraping:

- Review text
- Rating (1–5 stars)
- Review date
- Bank name
- Source platform

---

# Collection Summary

| Metric | Value |
|---|---|
| Total raw reviews collected | 11,495 |
| Final cleaned reviews | 8,328 |
| Number of banks analyzed | 3 |
| Source platform | Google Play Store |

---

# Project Structure

```text
fintech-review-analytics/

├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── data/
│   └── raw/
│
├── notebooks/
│
├── scripts/
│
├── sql/
│
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore