Fintech Review Analytics

Customer Experience Analytics for Ethiopian Fintech Applications

Project Overview

This project analyzes customer reviews collected from Ethiopian mobile banking applications available on the Google Play Store. The objective is to transform unstructured customer feedback into actionable business insights using data engineering, Natural Language Processing (NLP), sentiment analysis, thematic analysis, data visualization, and PostgreSQL database integration.

The project simulates a real-world analytics workflow that financial institutions and consulting firms can use to improve customer experience, mobile banking performance, product development, and retention strategies.

The analysis focuses on three major Ethiopian banks:

Commercial Bank of Ethiopia (CBE)
Bank of Abyssinia (BOA)
Dashen Bank
Business Problem

Mobile banking adoption in Ethiopia is increasing rapidly, and customer reviews on the Google Play Store have become one of the most valuable sources of direct customer feedback.

Customers regularly share experiences related to:

transaction failures
slow application performance
login and OTP issues
user interface usability
feature requests
customer support experiences
overall satisfaction or frustration

Without systematic analysis, this information remains unstructured and difficult for product teams to utilize effectively.

This project builds a complete analytics pipeline that transforms raw customer reviews into structured business intelligence capable of supporting product improvement decisions and customer experience strategies.

Business Scenarios

The project addresses three major business scenarios:

1. Retaining Users

Investigate whether recurring complaints such as slow transaction processing, failed transfers, and application crashes are systemic issues affecting customer retention across multiple banking applications.

2. Enhancing Features

Identify customer-requested features such as fingerprint login, faster transfers, improved user interface design, and fintech functionality to support future product development priorities.

3. Managing Complaints

Detect recurring technical complaints such as login failures and OTP verification problems to improve customer support prioritization and future AI chatbot integration strategies.

Project Objectives

The primary objectives of this project are:

Scrape customer reviews from the Google Play Store
Clean and preprocess review data
Perform sentiment analysis using transformer-based NLP models
Identify recurring themes and customer pain points
Store processed data in PostgreSQL
Generate visual insights and business recommendations
Simulate a real-world fintech analytics pipeline
Technologies Used

The project was developed using the following technologies:

Python
pandas
NumPy
google-play-scraper
Hugging Face Transformers
scikit-learn
spaCy
Matplotlib
Seaborn
PostgreSQL
SQLAlchemy
Git & GitHub
GitHub Actions
Dataset Information

Customer reviews were collected from the Google Play Store using the google-play-scraper Python library.

Applications Included
Bank	Application
Commercial Bank of Ethiopia	CBE Mobile Banking
Bank of Abyssinia	BOA Mobile Banking
Dashen Bank	Dashen Super App
Data Fields Collected

The following fields were collected during scraping:

Review text
Rating (1–5 stars)
Review date
Bank name
Source platform
Data Collection Summary
Bank	Reviews Collected
Commercial Bank of Ethiopia (CBE)	4,216
Bank of Abyssinia (BOA)	2,003
Dashen Bank	5,276
Metric	Value
Total raw reviews collected	11,495
Final cleaned reviews	8,328
Number of banks analyzed	3
Source platform	Google Play Store
Data Preprocessing

The following preprocessing steps were performed:

Removed duplicate reviews
Removed rows with missing review text or ratings
Normalized dates into YYYY-MM-DD format
Standardized text formatting
Prepared analysis-ready datasets

The cleaned dataset was exported as a CSV file for downstream analysis and database integration.

Sentiment Analysis

Sentiment analysis was performed using the transformer-based NLP model:

distilbert-base-uncased-finetuned-sst-2-english

The model was selected because it provides stronger contextual understanding and higher accuracy compared to lexicon-based methods such as VADER or TextBlob.

Each review was classified into:

Positive
Negative

along with a confidence score representing prediction certainty.

Key Sentiment Findings
CBE maintained relatively strong positive customer sentiment despite transaction-related complaints.
BOA showed the highest concentration of negative sentiment, mainly related to login and OTP issues.
Dashen Bank demonstrated balanced customer satisfaction with smoother user experience feedback.

The analysis revealed that transaction reliability, application stability, and authentication performance are the strongest drivers of customer satisfaction.

Thematic Analysis

Thematic analysis was performed using TF-IDF keyword extraction and manual grouping of semantically related keywords into business-relevant themes.

Main Themes Identified
Theme	Description
Transaction Performance	Slow transfers and failed transactions
Account Access Issues	Login failures and OTP problems
UI & Design	Interface usability and navigation
Customer Satisfaction	Positive user feedback
Feature Requests	Suggested improvements and new features
Example Keywords
Keywords	Theme
login error, OTP failed	Account Access Issues
slow transfer, delay	Transaction Performance
easy to use, clean interface	UI & Design
fingerprint login, dark mode	Feature Requests
PostgreSQL Database Integration

A PostgreSQL database named:

bank_reviews

was created to store processed review data in a structured relational format.

Database Tables
banks

Stores bank metadata:

bank_id
bank_name
app_name
reviews

Stores processed review data:

review_id
bank_id
review_text
rating
review_date
sentiment_label
sentiment_score
identified_theme
source
Database Setup
Step 1: Install PostgreSQL

Download PostgreSQL:

https://www.postgresql.org/download/

During installation:

Keep the default port 5432
Remember your PostgreSQL password
Step 2: Create Database

Create the database:

CREATE DATABASE bank_reviews;
Step 3: Run Schema File

Execute the schema file:

database/schema.sql

This creates:

banks table
reviews table
Step 4: Configure Database Connection

Update PostgreSQL credentials inside the insertion script:

engine = create_engine(
    "postgresql://postgres:your_password@localhost:5432/bank_reviews"
)
Step 5: Load Data into PostgreSQL

Run:

python scripts/load_to_postgres.py
Visualizations

The project includes several business-focused visualizations:

Sentiment distribution by bank
Rating distribution analysis
Word cloud visualization
Theme frequency analysis
Sentiment trends over time

These visualizations help identify major satisfaction drivers and recurring customer frustrations.

Key Insights
Commercial Bank of Ethiopia (CBE)
Strengths
Large customer adoption
Convenient banking services
Strong accessibility
Pain Points
Slow transaction processing
Occasional application crashes
Bank of Abyssinia (BOA)
Strengths
Functional mobile banking services
Pain Points
OTP verification failures
Login and authentication problems
Application instability
Dashen Bank
Strengths
Stable application performance
Smooth navigation experience
Pain Points
Occasional transaction delays
Limited feature innovation
Recommendations
Commercial Bank of Ethiopia (CBE)
Optimize transaction processing systems
Improve scalability during high traffic periods
Enhance crash monitoring infrastructure
Bank of Abyssinia (BOA)
Redesign authentication and OTP systems
Improve application stability
Prioritize bug fixing and customer support responsiveness
Dashen Bank
Introduce additional fintech features
Improve transaction handling under unstable network conditions
Continue investing in user experience improvements
Ethical Considerations and Limitations

Several limitations should be considered:

Customer reviews may overrepresent negative experiences
Only Android users on Google Play Store are represented
Some reviews contained mixed languages and emojis
Transformer models may misinterpret sarcasm or informal language
Review availability changes dynamically over time

Despite these limitations, the dataset provides valuable customer experience insights for Ethiopian fintech applications.

Project Structure
fintech-review-analytics/

├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── data/
│   └── raw/
│
├── database/
│   └── schema.sql
│
├── notebooks/
│
├── scripts/
│   ├── scrape_reviews.py
│   └── load_to_postgres.py
│
├── tests/
│
├── README.md
├── requirements.txt
├── requirements-dev.txt
└── .gitignore
Future Improvements

Potential future improvements include:

Multilingual sentiment analysis for Amharic reviews
Real-time review monitoring pipelines
Interactive dashboards using Power BI or Tableau
Advanced topic modeling techniques
AI-powered customer support analytics
Deployment as a cloud-based analytics platform