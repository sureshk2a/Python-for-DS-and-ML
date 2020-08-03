import seaborn as sns
import requests
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd
netflixDataset = pd.read_csv("C:/Users/suresha/PycharmProjects/Python-for-DS-and-ML/Files/netflixTVShows.csv")
print(netflixDataset.info())
sns.distplot(netflixDataset["type"])
plt.show()