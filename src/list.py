import pandas as pd
df = pd.read_csv("dataset/best_cheese.csv", sep = ',', error_bad_lines=False) #CSV Importing

print(df)

import numpy as np

print(df["Name"].values)