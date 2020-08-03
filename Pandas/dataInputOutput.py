from sqlalchemy import create_engine
import lxml
import html5lib
import bs4
import numpy as np
import pandas as pd
from numpy.random import randn
#df = pd.read_html("http://www.fdic.gov/bank/individual/failed/banklist.html")
df = pd.read_excel(r"C:\Users\suresha\PycharmProjects\Python-for-DS-and-ML\Files\Excel_Sample.xlsx",sheet_name="Sheet1")
print(df)
#df.to_csv(r"My_output",index=False)
engine = create_engine("sqlite:///:memory:")
df.to_sql("my_table",engine)
sqldf = pd.read_sql("my_table",con=engine)
print(sqldf)
