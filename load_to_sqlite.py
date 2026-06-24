import pandas as pd
from sqlalchemy import create_engine

# Create database
engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

# Read cleaned file
df = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

# Load into database
df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("Database loaded successfully")