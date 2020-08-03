import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
print(tips.head())

#distplot accepts one single column - Histogram
# sns.distplot(tips["total_bill"],kde= False,bins=30)
#Jointplot accepts two axes names and a dataset
#Draw a plot of two variables with bivariate and univariate graphs.
# sns.jointplot(x="total_bill", y="tip",data=tips,kind="kde")
# plt.show()

#Plot pairwise relationships in a dataset
# sns.pairplot(tips,hue="sex") #use hue only to columns that can be categorised
# plt.show()

#Plot datapoints in an array as sticks on an axis.
# sns.rugplot(tips["total_bill"])
# plt.show()

#Flexibly plot a univariate distribution of observations
# sns.distplot(tips["total_bill"],kde=False)
# plt.show()
