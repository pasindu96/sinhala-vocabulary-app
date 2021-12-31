import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import seaborn as sb
import matplotlib.pyplot as plt

sb.set_theme(style="whitegrid")

data = pd.read_excel(r'./Dataset/DataSet_Analyse.xlsx')
# print(data.to_string())

# engine = create_engine('mysql+pymysql://root:@localhost:3306/db_research?charset=utf8')
# data.to_sql('vocabulary_test_1', con=engine,  if_exists='replace')

# Load the example diamonds dataset
diamonds = sb.load_dataset("diamonds")

# Draw a scatter plot while assigning point colors and sizes to different
# variables in the dataset
f, ax = plt.subplots(figsize=(6.5, 6.5))
sb.despine(f, left=True, bottom=True)
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
sb.scatterplot(x="carat", y="price",
               hue="clarity", size="depth",
               palette="ch:r=-.2,d=.3_r",
               hue_order=clarity_ranking,
               sizes=(1, 8), linewidth=0,
               data=diamonds, ax=ax)

plt.show()
