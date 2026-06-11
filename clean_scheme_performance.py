"""
Scheme performance data cleaning script.

Tasks:
- Validate return metrics
- Validate risk metrics
- Check expense ratios
- Handle missing values
- Export cleaned scheme performance dataset
"""
import pandas as pd

perf = pd.read_csv("data/raw/07_scheme_performance.csv")

numeric_cols = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct',
    'benchmark_3yr_pct',
    'alpha',
    'beta',
    'sharpe_ratio',
    'sortino_ratio',
    'std_dev_ann_pct',
    'max_drawdown_pct',
    'aum_crore',
    'expense_ratio_pct'
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(perf[col], errors='coerce')

perf = perf[(perf['expense_ratio_pct'] >= 0.1) & (perf['expense_ratio_pct'] <= 2.5)]

print("Morningstar Rating Distribution:")
print(perf['morningstar_rating'].value_counts())

print("\nInvalid AMFI Codes:")
print(pd.to_numeric(perf['amfi_code'], errors='coerce').isna().sum())

perf = perf.drop_duplicates()

perf.to_csv("data/processed/clean_scheme_performance.csv", index=False)

print("\nScheme Performance cleaned successfully!")

print("\nExpense Ratio Summary:")
print(perf['expense_ratio_pct'].describe())