from re import I
import quandl as qd
import pandas as pd
import numpy as np

qd.ApiConfig.api_key = "DbJxfq6gcxYt6NXAZVy6"

## WTI Crude Oil Prices
print("\nWTI Crude Oil Prices\n")

# Std display
my_data = qd.get("EIA/PET_RWTC_D")
print(my_data)

# NumPy display
my_data = qd.get("EIA/PET_RWTC_D", returns="numpy")
print(my_data)

## US GDP Data
print("\nUS GDP Data\n")
my_data = qd.get("FRED/GDP", start_date="2019-12-31", end_date="2020-9-26")
print(my_data)

df = pd.DataFrame(my_data, columns=["Date", "Value"])
df.to_csv("GDP.csv")