import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set_style("darkgrid")
titanic = sns.load_dataset("titanic")
print(titanic.head())
print(titanic.info())

#sns.jointplot(x="fare",y="age",data=titanic)
#sns.distplot(titanic["fare"],kde=False) #for single column in dataset
#sns.boxplot(x="class",y="age",data=titanic,palette="rainbow")
#sns.swarmplot(x="class",y="age",data=titanic,palette="Set2")
#sns.countplot(x="sex",data=titanic)
# cor = titanic.corr()
# sns.heatmap(cor,cmap="coolwarm")
# plt.title("titanic.corr()")

# s =  sns.FacetGrid(data=titanic,col="sex")
# s.map(plt.hist,"age")

plt.show()