import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

pd.read_csv(
    "data/processed/nav_history_clean.csv"
).to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
).to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
).to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/raw/aum.csv"
).to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("All tables loaded successfully")