import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

print("Get a look at the data!")
print(iris.data)
print(iris.data.shape)
print(iris.data[0])

print()

print("Get a look at target data!")
print(iris.target)
print(iris.target.shape)
print(iris.target_names)
print(iris.target[0])

print()

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
for class_number in np.unique(iris.target):
    plt.figure(1)
    iris_df['sepal length (cm)'].iloc()
plt.show()
