import pandas as pd

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

print("All processed files created")