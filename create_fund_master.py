import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

meta = data["meta"]

df = pd.DataFrame([{
    "scheme_code": meta["scheme_code"],
    "scheme_name": meta["scheme_name"],
    "fund_house": meta["fund_house"],
    "scheme_type": meta["scheme_type"],
    "scheme_category": meta["scheme_category"]
}])

df.to_csv(
    "data/raw/fund_master.csv",
    index=False
)

print("fund_master.csv created")