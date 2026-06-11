# Mutual Fund Analytics Platform

## Project Overview

The Mutual Fund Analytics Platform is an end-to-end data analytics project developed to analyze mutual fund performance, investor behavior, SIP trends, and risk metrics. The project integrates data engineering, SQL, exploratory data analysis, performance analytics, advanced risk analytics, and Power BI dashboarding into a single analytics solution.

The objective is to help investors and analysts understand fund performance, risk exposure, investor participation patterns, and market trends through data-driven insights and interactive visualizations.

---

## Business Objective

The mutual fund industry generates large volumes of performance and investor-related data. Analyzing this data can help:

* Evaluate fund performance across multiple time horizons
* Measure risk-adjusted returns
* Monitor SIP inflows and investor activity
* Compare funds against benchmark indices
* Identify investor retention and continuity patterns
* Support fund recommendation decisions based on risk appetite

---

## Dataset Description

The project uses 10 datasets:

| Dataset                      | Description                    |
| ---------------------------- | ------------------------------ |
| 01_fund_master.csv           | Mutual fund master information |
| 02_nav_history.csv           | Historical NAV data            |
| 03_aum_by_fund_house.csv     | AUM by fund house              |
| 04_monthly_sip_inflows.csv   | Monthly SIP inflows            |
| 05_category_inflows.csv      | Category-wise inflows          |
| 06_industry_folio_count.csv  | Industry folio statistics      |
| 07_scheme_performance.csv    | Fund performance metrics       |
| 08_investor_transactions.csv | Investor transaction records   |
| 09_portfolio_holdings.csv    | Portfolio allocation details   |
| 10_benchmark_indices.csv     | Benchmark index data           |

---

## Project Architecture

Raw Data → Data Cleaning → SQLite Database → SQL Analysis → EDA → Performance Analytics → Advanced Analytics → Power BI Dashboard

---

## Project Structure

```text
mutual_fund_analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── clean_nav_history.py
├── clean_investor_transactions.py
├── clean_scheme_performance.py
├── data_ingestion.py
├── load_data.py
├── live_nav_fetch.py
├── recommender.py
├── run_pipeline.py
│
└── README.md
```

---

## ETL Pipeline

### Extraction

* Raw datasets loaded from CSV files
* NAV data collected and validated

### Transformation

* Missing value handling
* Date standardization
* Data validation
* Duplicate removal

### Loading

* Cleaned datasets loaded into SQLite database
* Tables created using schema.sql

---

## Database Design

The project uses SQLite as the backend database.

Major tables include:

* fund_master
* nav_history
* aum_by_fund_house
* monthly_sip_inflows
* category_inflows
* industry_folio_count
* scheme_performance
* investor_transactions
* portfolio_holdings
* benchmark_indices

---

## Exploratory Data Analysis

Performed analysis on:

* NAV trends
* SIP inflows
* Category inflows
* Investor demographics
* Portfolio allocation
* Benchmark performance
* Correlation analysis

More than 15 visualizations were created and exported.

---

## Performance Analytics

Implemented key mutual fund performance metrics:

* Daily Returns
* CAGR (1Y, 3Y, 5Y)
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Tracking Error
* Fund Scorecard

Generated outputs:

* fund_scorecard.csv
* alpha_beta.csv
* tracking_error.csv
* benchmark_comparison.png

---

## Advanced Analytics

Implemented advanced risk and investor analytics:

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* HHI Portfolio Concentration
* Mutual Fund Recommender

Generated outputs:

* var_cvar_report.csv
* rolling_sharpe_chart.png
* recommender.py

---

## Power BI Dashboard

Interactive dashboard pages include:

### Industry Overview

* AUM trends
* SIP inflows
* Folio statistics

### Fund Performance

* Risk vs Return
* Benchmark comparison
* Fund scorecard

### Investor Analytics

* Investor demographics
* Transaction analysis

### SIP & Category Analytics

* SIP inflow trends
* Category performance

### NAV Trend Dashboard

* Historical NAV analysis

---

## Key Findings

* Risk-adjusted metrics provide better evaluation than absolute returns.
* Some funds deliver superior Sharpe and Sortino ratios despite moderate returns.
* Investor participation varies significantly across categories.
* SIP continuity is a strong indicator of investor retention.
* Portfolio concentration differs considerably across schemes.

---

## How to Run

### Run ETL Pipeline

```bash
python run_pipeline.py
```

### Launch Notebooks

```bash
jupyter notebook
```

### Run Recommender

```bash
python recommender.py
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SQLite
* SQL
* Jupyter Notebook
* Power BI
* Git
* GitHub

---

## Future Improvements

* Live mutual fund API integration
* Predictive NAV forecasting
* Advanced recommendation engine
* Real-time dashboard updates
* Portfolio optimization models

---

## Author

Rohit M

Mutual Fund Analytics Capstone Project
