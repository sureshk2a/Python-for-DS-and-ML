import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df3 = pd.read_csv("..//Files/df3.csv")
print(df3.info())
print(df3.head())
#df3.plot.scatter(x="a",y="b",color="#FF0000",figsize=(10,3))
#df3["a"].plot.hist()

#plt.style.use("ggplot")
#df3["a"].plot.hist(bins=20,alpha=0.5) #alpha is transperent

#df4 = np.split(df3,[2],axis=1)
#df4[0].plot.box(whiskerprops= dict(linestyle='--' , linewidth=2))
#df3[["a","b"]].plot.box()
#df3["d"].plot.kde(lw=5,ls="--")
#df3.iloc[:30].plot.area(cmap="coolwarm")
#plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()