import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

files = [
    "Axis_Bluechip",
    "ICICI_Bluechip",
    "Kotak_Bluechip",
    "Nippon_Large_Cap",
    "SBI_Bluechip",
    "fund_master",
    "aum"
]

for file in files:
    df = pd.read_csv(f"data/raw/{file}.csv")
    df.to_csv(
        f"data/processed/{file}_clean.csv",
        index=False
    )

print("All cleaned files created successfully.")