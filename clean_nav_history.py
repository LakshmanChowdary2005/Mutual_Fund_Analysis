import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv("data/raw/nav_history.csv")

df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")

df = df.sort_values("date")
df = df.drop_duplicates()
df = df[df["nav"] > 0]

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("Clean file created successfully")