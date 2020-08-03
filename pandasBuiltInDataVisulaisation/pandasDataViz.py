import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df1 = pd.read_csv("../Files/df1.csv",index_col=0)
print(df1.head())
df2 = pd.read_csv("../Files/df2.csv")
print(df2.head())
#df1["A"].plot.hist(bins=30)
#df2.plot.area()
#df1.plot.scatter(x="A",y="B",c="C",cmap="coolwarm") #scatter plot with a value indicator
#df2.plot.box()
df = pd.DataFrame(np.random.randn(1000,2),columns=["a","b"])
df.plot.hexbin(x="a",y="b")
df2.plot.density()
plt.show()