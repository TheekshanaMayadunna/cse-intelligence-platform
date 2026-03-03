# CSE Intelligence Platform

An automated equity research engine for the Colombo Stock Exchange (CSE),
combining data engineering pipelines, machine learning models, and an
interactive analytics dashboard.

**Live Dashboard:** [link — add after deployment]
**Built for:** Financial sector internship portfolio project

---

## What This Does

This platform automatically collects daily stock prices, macroeconomic
indicators, and financial news for 8 major CSE-listed companies. It applies
machine learning models to forecast prices, detect market anomalies, and
score news sentiment — then presents all insights through a professional
Streamlit dashboard with auto-generated PDF research reports.

---

## Architecture
```
Data Sources → Ingestion Layer → PostgreSQL → Transformation → ML Models → Dashboard
    (CSE, CBSL,     (Python +                    (Pandas,        (Prophet,    (Streamlit)
     News RSS)       Airflow)                      dbt)         IsolationForest,
                                                               FinBERT)
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| Data Ingestion | Python, yfinance, BeautifulSoup, feedparser, Apache Airflow |
| Storage | PostgreSQL 15, SQLAlchemy |
| Transformation | Pandas, pandas-ta, NumPy |
| Machine Learning | Prophet, Scikit-learn, FinBERT, VADER |
| Dashboard | Streamlit, Plotly |
| Reports | fpdf2 |
| DevOps | Docker, Git, GitHub |

---

## Target Stocks

JKH, COMB, DIAL, NEST, LION, SAMP, HHL, MELS

---

## Setup Instructions

1. Clone this repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and fill in your database credentials
6. Create the database: run `sql/schema.sql` in pgAdmin against a PostgreSQL 15 instance
7. Test connection: `python db.py`
8. Run dashboard locally: `streamlit run dashboard/app.py`

---

## Project Status

- [x] Phase 1: Environment setup, schema, project structure
- [ ] Phase 2: Data ingestion pipelines
- [ ] Phase 3: Feature engineering
- [ ] Phase 4: ML models
- [ ] Phase 5: Dashboard
- [ ] Phase 6: Deployment

---

## Author

[Theekshana Mayadunna] 