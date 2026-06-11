"""
Fund master exploratory analysis script.

Tasks:
- Explore fund categories
- Analyse AMC distribution
- Review fund attributes
- Generate summary statistics
"""
import pandas as pd

df = pd.read_csv('data/raw/01_fund_master.csv')
nav = pd.read_csv('data/raw/02_nav_history.csv')

print("="*50)
print("FUND MASTER EXPLORATION")
print("="*50)

print(f"\nUnique Fund Houses: {df['fund_house'].nunique()}")
print(df['fund_house'].unique())

print(f"\nUnique Categories: {df['category'].nunique()}")
print(df['category'].unique())

print(f"\nUnique Sub-Categories: {df['sub_category'].nunique()}")
print(df['sub_category'].unique())

print(f"\nUnique Risk Grades: {df['risk_category'].nunique()}")
print(df['risk_category'].unique())

print("\n" + "="*50)
print("AMFI CODE VALIDATION")
print("="*50)

fund_codes = set(df['amfi_code'].unique())
nav_codes = set(nav['amfi_code'].unique())

missing = fund_codes - nav_codes
print(f"\nTotal AMFI codes in fund_master: {len(fund_codes)}")
print(f"Total AMFI codes in nav_history: {len(nav_codes)}")
print(f"Missing codes in nav_history: {len(missing)}")

print("\n DATA QUALITY SUMMARY:")
print(f"  - fund_master has {len(df)} records")
print(f"  - nav_history has {len(nav)} records")
print(f"  - {len(missing)} AMFI codes not found in nav_history")
