import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

tables = [
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

for table in tables:
    query = f"SELECT COUNT(*) as rows FROM {table}"
    df = pd.read_sql(query, conn)

    print("\n", "="*40)
    print(table)
    print(df)

conn.close()