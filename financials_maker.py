import pandas as pd
import numpy as np

data_raw = pd.read_csv('./data/mining_2008.csv', encoding = "cp1252")

print(data_raw.info())