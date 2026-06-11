"""
Data ingestion script for the Mutual Fund Analytics project.

Tasks:
- Read all raw datasets
- Validate file availability
- Perform initial schema checks
- Prepare data for cleaning and processing
"""
import pandas as pd
import os

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

anomalies = []

for file in files:
    path = f"data/raw/{file}"
    print(f"\n{'='*50}")
    print(f"Loading: {file}")
    df = pd.read_csv(path)
    
    print(f"Shape: {df.shape}")
    print(f"Dtypes:\n{df.dtypes}")
    print(f"Head:\n{df.head()}")
    
    nulls = df.isnull().sum().sum()
    if nulls > 0:
        anomalies.append(f"{file}: {nulls} missing values")

print("\n" + "="*50)
print("ANOMALIES FOUND:")
if anomalies:
    for a in anomalies:
        print(f"  - {a}")
else:
    print("  No anomalies found!")

print("\nData ingestion complete! ✅")