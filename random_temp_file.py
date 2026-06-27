import pandas as pd

df =pd.read_csv("data/raw/international_matches1.csv")

print(df.shape)
print(df.columns.tolist())
