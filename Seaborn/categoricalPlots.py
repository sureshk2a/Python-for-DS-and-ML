import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
tips = sns.load_dataset('tips')
print(tips.head())

#barplot
# sns.barplot(x="sex",y="total_bill",data=tips,estimator=np.std) #avarage total bill between male and females
# plt.show()

#countplot - count uniques and plot in grpah
# sns.countplot(x="sex",data=tips)
# plt.show()

#boxplot - shows distribution of categorical data
# sns.boxplot(x="day",y="total_bill",data=tips)
# plt.show()

##Violinplot
# sns.violinplot(x="day",y="total_bill",data=tips,hue="sex",split=True)
# plt.show()

##stripplot
# sns.stripplot(x="day",y="total_bill",data=tips,hue="sex")
# plt.show()

# sns.swarmplot(x="day",y="total_bill",data=tips,hue="sex")
# plt.show()

# sns.factorplot(x="day",y="total_bill",data=tips,kind="bar",hue="sex")
# plt.show()









