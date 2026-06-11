"""
Mutual Fund Recommendation Engine.

Input:
- Risk Appetite (Low, Moderate, High)

Output:
- Top 3 recommended funds
- Ranked using Sharpe Ratio
- Filtered by risk profile
"""
import pandas as pd
perf = pd.read_csv("data/raw/07_scheme_performance.csv")
risk = input("Enter Risk Appetite (Low/Moderate/High): ").strip().title()
filtered = perf[perf['risk_grade'] == risk]
recommendations = (filtered.sort_values('sharpe_ratio', ascending=False).head(3))
print("\nTop 3 Recommended Funds\n")
print(
    recommendations[
        [   
            'amfi_code',
            'scheme_name',
            'risk_grade',
            'sharpe_ratio'
        ]
    ]
)