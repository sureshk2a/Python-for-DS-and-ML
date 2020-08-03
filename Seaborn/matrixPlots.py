import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
flights = sns.load_dataset('flights')
tips = sns.load_dataset('tips')
tc = tips.corr()

# sns.heatmap(tc,annot=True)
# plt.show()
fp = flights.pivot_table(index="month",columns="year",values="passengers")
# print(fp)
# sns.heatmap(fp,cmap="magma",linecolor="white",linewidths=.5)
# plt.show()

#
# sns.clustermap(fp)
# plt.show()