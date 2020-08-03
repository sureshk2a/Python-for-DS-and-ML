import chart_studio.plotly as py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotly import __version__ as version
import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
cf.go_offline()
df = pd.DataFrame(np.random.randn(100,4),columns="A B C D".split())
print(df.head())
df2 = pd.DataFrame({"Category":["A","B","C"],"Values":[32,43,50]})
print(df2)
df.iplot()
plt.show()
