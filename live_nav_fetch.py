import requests
import pandas as pd
import os

schemes = {
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

os.makedirs("data/raw", exist_ok=True)

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    print(f"Fetching {name}...")
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data['data'])
    df['fund_name'] = data['meta']['scheme_name']
    df.to_csv(f"data/raw/{name}_nav.csv", index=False)
    print(f"Saved {name}_nav.csv ✅")

print("\nAll NAV data fetched successfully!")