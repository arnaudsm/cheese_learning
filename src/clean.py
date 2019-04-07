import pandas as pd 
from pathlib import Path

df = pd.read_csv("dataset/frenchcheese.csv", sep = ';', error_bad_lines=False)  
df = df.drop(columns=["Geo Shape"], axis=1)
df['index'] = df.index

print(df.head())

