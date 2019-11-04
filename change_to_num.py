import pandas as pd
import re

data = pd.read_csv('Orders.csv')
data.Profit = [re.sub('[$,]','',x) for x in data.Profit]
data.Sales = [re.sub('[$,]','',x) for x in data.Sales]
data.Profit = pd.to_numeric(data.Profit)
data.Sales = pd.to_numeric(data.Sales)

