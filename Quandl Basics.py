from re import I
import quandl as qd
import pandas as pd
import numpy as np

qd.ApiConfig.api_key = "DbJxfq6gcxYt6NXAZVy6"

# Std display
my_data = qd.get("EIA/PET_RWTC_D")
print(my_data)

# NumPy display
my_data = qd.get("EIA/PET_RWTC_D", returns="numpy")
print(my_data)

