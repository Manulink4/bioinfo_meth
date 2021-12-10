import pandas as pd

df = pd.read_csv("meth_counts/GSE153594_Methylation_Counts.csv", sep=",", decimal=".", dtype="object")
# print(df)

df = df[["Chr", "Start", "End", "NZM9"]]






