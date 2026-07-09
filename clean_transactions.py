import pandas as pd
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# Read transactions file
df = pd.read_csv("data/raw/investor_transactions.csv")

# Remove duplicate header row if present
df = df[df["investor_id"] != "investor_id"]

# Remove leading/trailing spaces
df.columns = df.columns.str.strip()

# Convert amount to numeric
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# Convert transaction date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    format="%d-%m-%Y",
    errors="coerce"
)

# Remove rows with invalid values
df = df.dropna(subset=["transaction_date", "amount"])

# Reset index
df = df.reset_index(drop=True)

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned successfully!")
print(df.head())