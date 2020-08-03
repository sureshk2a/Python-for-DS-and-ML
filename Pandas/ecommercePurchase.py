import numpy as np
import pandas as pd
from numpy.random import randn


def try_cutoff(x):
    try:
        return round(float(x), 3)
    except Exception:
        return x


data = pd.read_csv(r"C:\Users\suresha\PycharmProjects\Python-for-DS-and-ML\Files\Ecommerce Purchases.csv")
data.head()
print(data.info())
print(data["Purchase Price"].mean())  # average of purchase price
print(data["Purchase Price"].min())  # minimum purchase price
print(data["Purchase Price"].max())  # maximum purchase price
print(len(data[data["Language"] == "en"]))  # total people having english as their common language on site
print(len(data[data["Job"] == "Lawyer"]))  # total people having job title as lawyer
print(data.groupby("AM or PM").nunique())  # how many people purchased in AM and PM
print(data["Job"].value_counts().head(5))  # 5 most common job title
print(data[data["Lot"] == "90 WT"]["Purchase Price"])  # Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction
print(data[try_cutoff(data["Credit Card"]) == 4926535242672853]["Email"])  # email of the person with the following Credit Card Number: 4926535242672853
print(data[(data["CC Provider"] == "American Express") & (data["Purchase Price"] > 95)])  # How many people have American Express as their Credit Card Provider *and made a purchase above $95
purch2025 = data["CC Exp Date"].apply(lambda exp : exp[3:]=='25') #w many people have a credit card that expires in 2025?
print(len(data[purch2025]))
print(data["Email"].apply(lambda mail : mail.split("@")[1]).value_counts().head(5)) #What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)
