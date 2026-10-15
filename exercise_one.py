"""
Some of this code contains missing ("Marked with TODO) or incorrect information and will not run. Correct the errors.
"""


import pandas as pd

csv_path = "" # TODO: write a path to your csv file - normal path files are "./folder/filename.csv"
column = "" # TODO: any numeric column in your csv


def load_data(path):
    df = pd.read_csv(path)
    return df


def summarize(df, column): # there are two errors in this function
    print("Rows:", len(df))
    print("Mean:", df[column].mean()
    print("Max:", df[column].max())
    print("Min:", df[column].mn())


def main(): #there are three errors in this function
    df = load_data(CSV_PATH)
    summarize(dataframe, COLUMN)


if __name__ == "__main__":
    main()