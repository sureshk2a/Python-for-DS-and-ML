import seaborn as sns
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
movieDataset = pd.read_csv("C:/Users/suresha/PycharmProjects/Python-for-DS-and-ML/Files/netflix_titles.csv")

print(movieDataset.info())


indianMovies = movieDataset[(movieDataset["type"] == "Movie") & (movieDataset["country"].str.contains("India"))]
print(indianMovies)

sns.swarmplot(x="director",y="releaseyear",data=indianMovies,hue="rating")
plt.show()
