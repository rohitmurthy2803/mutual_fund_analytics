# Data Dictionary

## NAV History Dataset

| Column    | Data Type | Description                    |
| --------- | --------- | ------------------------------ |
| amfi_code | INTEGER   | Unique mutual fund scheme code |
| date      | DATE      | NAV record date                |
| nav       | REAL      | Net Asset Value of the scheme  |

## Investor Transactions Dataset

| Column             | Data Type | Description                         |
| ------------------ | --------- | ----------------------------------- |
| investor_id        | TEXT      | Unique investor identifier          |
| transaction_date   | DATE      | Date of transaction                 |
| amfi_code          | INTEGER   | Mutual fund scheme code             |
| transaction_type   | TEXT      | SIP, Lumpsum or Redemption          |
| amount_inr         | REAL      | Transaction amount in Indian Rupees |
| state              | TEXT      | Investor state                      |
| city               | TEXT      | Investor city                       |
| city_tier          | TEXT      | Tier classification of city         |
| age_group          | TEXT      | Investor age category               |
| gender             | TEXT      | Investor gender                     |
| annual_income_lakh | REAL      | Annual income in lakhs              |
| payment_mode       | TEXT      | Mode of payment                     |
| kyc_status         | TEXT      | KYC verification status             |

## Scheme Performance Dataset

| Column             | Data Type | Description                          |
| ------------------ | --------- | ------------------------------------ |
| amfi_code          | INTEGER   | Mutual fund scheme code              |
| morningstar_rating | INTEGER   | Morningstar rating (1-5)             |
| return_1yr_pct     | REAL      | One-year return percentage           |
| return_3yr_pct     | REAL      | Three-year return percentage         |
| return_5yr_pct     | REAL      | Five-year return percentage          |
| benchmark_3yr_pct  | REAL      | Benchmark return percentage          |
| alpha              | REAL      | Alpha performance metric             |
| beta               | REAL      | Beta risk metric                     |
| sharpe_ratio       | REAL      | Risk-adjusted return metric          |
| sortino_ratio      | REAL      | Downside-risk-adjusted return metric |
| std_dev_ann_pct    | REAL      | Annualized standard deviation        |
| max_drawdown_pct   | REAL      | Maximum drawdown percentage          |
| aum_crore          | REAL      | Assets Under Management (Crores)     |
| expense_ratio_pct  | REAL      | Fund expense ratio percentage        |
