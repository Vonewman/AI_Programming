from scipy.sparse.construct import rand
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# load the data
iris_dataset = load_iris()

# Define X and y
X, y = iris_dataset['data'], iris_dataset['target']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Building a k-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=1)

# Train the model
knn.fit(X_train, y_train)

# Evaluating the Model
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))