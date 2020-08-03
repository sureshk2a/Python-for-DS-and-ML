import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("../Files/911.csv") #Read csv to dataframe
#print(df.info()) #Get the info on dataframe
#print(df["zip"].value_counts().head(5)) #What are the top 5 zipcodes for 911 calls?
#print(df["twp"].value_counts().head(5)) #What are the top 5 townships (twp) for 911 calls?
#print(df["title"].nunique()) #how many unique title codes are there?
df["Reason"] = df["title"].apply(lambda x : str(x).split(":")[0]) #In the titles column there are "Reasons/Departments" specified before the title code.
# These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.
#print(df["Reason"])
#print(df["Reason"].value_counts()) #What is the most common Reason for a 911 call based off of this new column?
#sns.countplot(x="Reason",data=df,palette="deep") #Now use seaborn to create a countplot of 911 calls by Reason.
dateTime = pd.to_datetime(df["timeStamp"])
#print(dateTime)
#create 3 new columns called Hour, Month, and Day of Week. You will create these columns based off of the timeStamp column
df["Hour"] = dateTime.apply(lambda x : x.hour)
df["Month"] = dateTime.apply(lambda x : x.month)
df["Day"] = dateTime.apply(lambda  x : x.dayofweek)
#print(df["Hour"])
# Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week:
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
#print(df["Month"])
df["Day"] = df["Day"].map(dmap)
#sns.countplot(x="Day",hue="Reason",data=df) #seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column
#sns.countplot(x="Month",hue="Reason",data=df)
# create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head()
# method on this returned DataFrame.
monthCountBy = df.groupby("Month").count()
#monthCountBy["twp"].plot()
#sns.lmplot(x="Month",y="twp",data=monthCountBy.reset_index())
df["Date"] = dateTime.apply(lambda x: x.date())
groupByDate = df.groupby("Date").count()
#groupByDate["twp"].plot() #groupby this Date column with the count() aggregate and create a plot of counts of 911 calls?
#plt.tight_layout()
#print(groupByDate)
def reasonPlot(reason):
    df[df["Reason"] == reason].groupby("Date").count()["twp"].plot()
    plt.title(reason)
#reasonPlot("Traffic")
#reasonPlot("Fire")
#reasonPlot("EMS")
print(df.info())
heatGrouped = df.groupby(by=["Day","Hour"]).count()["Reason"].unstack() #Setting columns and index
sns.heatmap(heatGrouped,cmap="viridis",linecolor="white",linewidths=.5)
sns.clustermap(heatGrouped,cmap="viridis")
plt.show()