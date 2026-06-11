"""
NAV history data cleaning script.

Tasks:
- Convert dates to standard format
- Sort NAV records by fund and date
- Remove duplicates
- Handle missing values
- Generate cleaned NAV dataset
"""
import pandas as pd
nav = pd.read_csv("data/raw/02_nav_history.csv")
nav['date'] = pd.to_datetime(nav['date'])
nav = nav.sort_values(['amfi_code', 'date'])
nav = nav.drop_duplicates()
nav = nav[nav['nav'] > 0]
nav['nav'] = nav.groupby('amfi_code')['nav'].ffill()
nav.to_csv(
    "data/processed/clean_nav_history.csv",
    index=False
)
print("NAV History cleaned successfully!")