import pandas as pd
from datetime import datetime

orders = pd.read_csv('data/Orders.csv')

orders['Order.Date'] = list(map(lambda x: datetime.strptime(x, '%m/%d/%y').date(), orders['Order.Date']))
orders['order_month'] = list(map(lambda x: x.month, orders['Order.Date']))
orders['order_year'] = list(map(lambda x: x.year, orders['Order.Date']))

print(orders.head())