import pandas as pd

df = pd.read_csv("data/raw/scheme_performance.csv")

for col in ["return_1y", "return_3y", "return_5y"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df[
    (df["expense_ratio"] >= 0.1)
    &
    (df["expense_ratio"] <= 2.5)
]

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned successfully")