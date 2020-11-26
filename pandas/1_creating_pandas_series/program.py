import pandas as pd


groceries = pd.Series(data=[30, 6, 'Yes', 'No'],
                      index=['eggs', 'apples', 'milk', 'bread'])
print(groceries)
print('Groceries has shape: ', groceries.shape)
print('Groceries has dimension: ', groceries.ndim)
print('Groceries has a total of: ', groceries.size, ' elements')
print('The data in Groceries is: ', groceries.values)
print('THe index of Groceries is: ', groceries.index)


# We check whether bananas is a food item (an index) in Groceries
x = 'bananas' in groceries

y = 'bread' in groceries


print('Is bananas an index label in Groceries:', x)
print('Is bread an index label in Groceries:', y)
