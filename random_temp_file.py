import pandas as pd

df =pd.read_csv("data/raw/international_matches1.csv")

# print(df.shape)
# print(df.columns.tolist())

# unique_tournaments = df["Tournament"].unique()
#
# for tournament in unique_tournaments:
#     print(tournament)

# tournament_counts = df["Tournament"].value_counts()
#
# print(tournament_counts)
with pd.option_context('display.max_rows', None):
    print(df["Tournament"].value_counts())
