import pandas as pd


def main():
    df = pd.read_csv("meth_counts/GSE153594_Methylation_Counts.csv", sep=",", decimal=".", dtype="object")
    df = df[["Chr", "Start", "End", "NZM9"]]
    print("Hello")


if __name__ == '__main__':
    main()
