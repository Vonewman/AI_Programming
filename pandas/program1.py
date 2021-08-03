# We import Pandas as pd into Python
import pandas as pd

# We create a Pandas Series that stores a grocery list
groceries = pd.Series(data=[30, 6, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])
print(groceries)

# we print some information about Groceries
print('Groceries has shape: ', groceries.shape)
print('Groceries has dimension: ', groceries.ndim)
print('Grocesries has a total of ', groceries.size, ' elements.')

x = 'bananas' in groceries

y = 'bread' in groceries

# We print results
print('Is bananas an index label in Groceries: ', x)
print('Is bread an index label in Groceries: ', y)