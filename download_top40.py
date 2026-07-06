import os
import time
import pandas as pd
import requests

# Read the 40 selected schemes
schemes = pd.read_csv("top40_schemes.csv")

# Create output folder
os.makedirs("data/raw/top40", exist_ok=True)

for _, row in schemes.iterrows():

    scheme_code = row["schemeCode"]
    scheme_name = row["schemeName"]

    print(f"Downloading {scheme_name}...")

    try:
        url = f"https://api.mfapi.in/mf/{scheme_code}"

        data = requests.get(url).json()

        if "data" not in data:
            print("Skipped")
            continue

        nav = pd.DataFrame(data["data"])

        filename = (
            scheme_name
            .replace("/", "_")
            .replace(":", "")
            .replace(" ", "_")
        )

        nav.to_csv(
            f"data/raw/top40/{filename}.csv",
            index=False
        )

        time.sleep(1)

    except Exception as e:
        print(e)