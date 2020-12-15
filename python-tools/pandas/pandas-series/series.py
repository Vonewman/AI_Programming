import pandas as pd


groceries = pd.Series(data=[30, 6, 'Yes', 'No'],
                      index=['eggs', 'apples', 'milk', 'bread'])


print(groceries)
print('Groceries has shape: ', groceries.shape)
print('Groceries has dimension: ', groceries.ndim)
print('Groceries has a total of ', groceries.size, ' elements')


print('The index in Groceries is: ', groceries.index)
print('THe data in Groceries is: ', groceries.values)


x = 'bananas' in groceries
y = 'bread' in groceries


print('Is bananas an index label in Groceries:', x)
print('Is bread an index label in Groceries: ', y)


# Accessing and Deleting Elements in Pandas Series
# We access elements in Groceries using index labels:


print('How many eggs do we need to buy: ', groceries['eggs'])
print()


# We can access multiple index labels
print('Do we need milk and bread:\n', groceries[['milk', 'bread']])
print()


# We use loc to acces index labels
print('How many eggs and apples do we need to buy:\n',
      groceries.loc[['eggs', 'apples']])


# We access elements in Groceries using numerical indices:
# We use multiple numerical indices
print('How many eggs and apples do we need to buy:\n', groceries[[0, 1]])
print()


# We use a negative numerical index
print('Do we need bread:\n', groceries[[-1]])
print()


# We use a single numerical index
print('How may eggs do we need to buy:', groceries[0])
print()
# We use iloc to access multiple numerical indices
print('Do we need milk and bread:\n', groceries.iloc[[2, 3]])
