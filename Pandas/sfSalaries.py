import numpy as np
import pandas as pd
from numpy.random import randn
sal = pd.read_csv(r"C:\Users\suresha\PycharmProjects\Python-for-DS-and-ML\Files\Salaries.csv")
sal.head()
print(sal.info()) #To get details about columns
#print(sal["BasePay"].mean()) #Average base pay
#print(sal["OvertimePay"].max()) #Maximum overtime pay paid
#print(sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"]) #Job title of JOSEPH DRISCOLL
#print(sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits"]) #Pay including benfits of JOSEPH DRISCOLL
#print(sal[sal["TotalPay"] == sal["TotalPay"].max()]) #Name of the highest paid employee
#print(sal[sal["TotalPay"] == sal["TotalPay"].min()]) #Name of the lowest paid employee
#print(sal["JobTitle"].nunique()) #total number of unique jobs
print(sal["JobTitle"].value_counts().head(5)) #alue_counts() function to find the values counts of each unique value in the given Series object.
#print(sal["JobTitle"].str.contains("Chief"))
print(sal[sal["JobTitle"].str.contains("Chief")]["JobTitle"])
print(sal.groupby("Year").mean()["BasePay"])

