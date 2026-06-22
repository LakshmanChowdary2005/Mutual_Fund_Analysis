import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)
data = response.json()

nav_df = pd.DataFrame(data["data"])

print(nav_df.head())  # Check before saving

nav_df.to_csv(
    "data/raw/nav_history.csv",
    index=False
)

print("Saved")