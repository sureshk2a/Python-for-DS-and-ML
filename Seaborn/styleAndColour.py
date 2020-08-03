import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
flights = sns.load_dataset('flights')
tips = sns.load_dataset('tips')
#sns.set_context(context="poster")
#sns.countplot(x="sex",data=tips,palette="seismic")
sns.lmplot(x="total_bill",y="tip",data=tips,hue="sex",palette="deep")
sns.despine()


plt.show()
