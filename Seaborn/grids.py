import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
flights = sns.load_dataset('flights')
tips = sns.load_dataset('tips')
iris = sns.load_dataset("iris")
print(iris.head())
print(iris["species"].unique())
# g = sns.PairGrid(iris)
g = sns.FacetGrid(data=tips,col="time",row="smoker")
g.map(plt.scatter,"total_bill","tip")
plt.show()