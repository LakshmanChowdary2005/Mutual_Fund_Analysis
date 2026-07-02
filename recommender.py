import pandas as pd

# Load scheme performance
performance = pd.read_csv("data/raw/scheme_performance.csv")

# Load fund master
fund_master = pd.read_csv("data/raw/fund_master.csv")

# Merge to get scheme names
funds = performance.merge(
    fund_master[["scheme_code", "scheme_name"]],
    on="scheme_code",
    how="left"
)

# Create risk grades (sample mapping)
risk_map = {
    125497: "High",
    119551: "Moderate",
    120503: "Moderate",
    128930: "Low",
    118834: "High"
}

funds["risk_grade"] = funds["scheme_code"].map(risk_map)

# Use 5-year return as a simple ranking metric
funds["Score"] = funds["return_5y"]

risk = input("Enter Risk Appetite (Low/Moderate/High): ")

recommendation = (
    funds[funds["risk_grade"] == risk]
    .sort_values("Score", ascending=False)
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")
print(
    recommendation[
        ["scheme_name", "risk_grade", "return_5y", "expense_ratio"]
    ]
)