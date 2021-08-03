# We import Pandas as pd into Python
import pandas as pd

# We create a Pandas Series that stores a grocery list
groceries = pd.Series(data=[30, 6, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])
print(groceries)

# We access elements in Groceries using index labels:

# We use a single index labe;
print('How many eggs do we need to buy: ', groceries['eggs'])
print()

# We can access multiple index labels
print('Do we need milk and bread:\n', groceries[['milk', 'bread']])
print()

# We use loc to access multiple index labels
print('How many index and labels do we need to buy:\n', groceries.loc[['milk', 'apples']])
print()

# We access element in Groceries using numerical indices:

# We use multiple numerical indices
print('How many apples and eggs do we need to buy:\n', groceries[[0, 1]])
print()

# We use a negative numerical index
print('Do we need bread:\n', groceries[[-1]])
print()


# We use a single
