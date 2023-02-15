import pandas as pd

# Read data files into pandas dataframes
data0 = pd.read_csv('data/daily_sales_data_0.csv')
data1 = pd.read_csv('data/daily_sales_data_1.csv')
data2 = pd.read_csv('data/daily_sales_data_2.csv')

data = pd.concat([data0, data1, data2], axis=0)

# remove any row which contains another type of product than pink morsel
data = data.where(data['product'] == 'pink morsel').dropna()

# add sales record to the 
data['sales'] = data.apply(lambda x: float(x['price'].split('$')[1]) * x['quantity'], axis=1)

# drop price, quantity and product columns 
data = data.drop(['price', 'quantity', 'product'], axis=1)

# write to csv

data.to_csv('data/pink_morsel_sales.csv')