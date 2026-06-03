import pandas as pd

txn = pd.read_csv("data/raw/08_investor_transactions.csv")

txn['transaction_date'] = pd.to_datetime(txn['transaction_date'])

txn['transaction_type'] = txn['transaction_type'].str.strip().str.title()

txn = txn[
    txn['transaction_type'].isin(
        ['Sip', 'Lumpsum', 'Redemption']
    )
]

txn = txn[txn['amount_inr'] > 0]

txn = txn.drop_duplicates()

txn.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("Investor Transactions cleaned successfully!")