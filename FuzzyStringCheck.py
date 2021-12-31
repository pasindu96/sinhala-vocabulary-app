import pandas as pd
from fuzzywuzzy import process


# file_loc = "path.xlsx"
# df = pd.read_excel(r'./Dataset/DataSet_Analyse.xlsx', index_col=None, na_values=['NA'], usecols="A")
#
# vocabularyList = []
#
# for index, row in df.iterrows():
#     vocabularyList.append(row['වචනය'])


def get_matches(word, choices):
    results = process.extract(word, choices, limit=1)
    return results


test = ["ගෝණා"]
word = "ගෝණා"

print(get_matches("ගණ", [word])[0][1])
