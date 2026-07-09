import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv("data/raw/investor_transactions.csv")

df["transaction_type"] = df["transaction_type"].str.upper()

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    format="%d-%m-%Y"
)

df = df[df["amount"] > 0]

valid_kyc = ["VERIFIED", "PENDING", "REJECTED"]

df = df[df["kyc_status"].isin(valid_kyc)]

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned successfully")