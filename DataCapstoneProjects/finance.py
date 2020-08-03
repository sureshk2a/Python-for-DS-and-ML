from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
start = datetime(2006, 1, 1)
end = datetime(2016, 1, 1)
#BAC = data.DataReader("BAC","google",start,end)
df = pd.read_pickle('../Files/all_banks')
print(df.info())
BAC = df["BAC"]
C = df["C"]
GS = df["GS"]
JPM = df["JPM"]
MS = df["MS"]
tickers = ["BAC","C","GS","JPM","MS"]
bank_stocks = pd.concat([BAC,C,GS,JPM,MS],keys=tickers,axis=1)
#print(bank_stocks.head())
bank_stocks.columns.names = ['Bank Ticker','Stock Info']
#print(bank_stocks)
#for tick in tickers:
    #print(tick,bank_stocks[tick]["Close"].max())
#print(bank_stocks.xs(key="Close",axis=1,level="Stock Info").max())
returns = pd.DataFrame()
for tick in tickers:
    returns[tick+' Return'] = bank_stocks[tick]["Close"].pct_change()
print(returns.head())
#sns.pairplot(returns[1:])
#print(returns.idxmin()) #worst single day return
#print(returns.idxmax()) #best single day return
#print(returns.std()) # standard deviation to find the risky stock
#print(returns.loc["2015-01-01":"2015-12-31"].std()) #find risky stocks on 2k15
print(returns.loc["2015-01-01":"2015-12-31"])
bank_stocks.xs(key="CLose",axis=1,level="Stock Info").plot()
plt.show()