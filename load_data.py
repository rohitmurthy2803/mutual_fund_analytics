"""
Database loading script.

Tasks:
- Connect to SQLite database
- Load cleaned datasets
- Insert records into database tables
- Verify successful data loading
"""
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

nav = pd.read_csv("data/processed/clean_nav_history.csv")
txn = pd.read_csv("data/processed/clean_investor_transactions.csv")
perf = pd.read_csv("data/processed/clean_scheme_performance.csv")

nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
txn.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Data loaded into SQLite successfully!")