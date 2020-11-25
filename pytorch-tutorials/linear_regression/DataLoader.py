# print("Starter: PyTorch - DataLoading tutorial on Kaggle")
import pandas as pd

nRowsRead = 1000


df1 = pd.read_csv('faces/face_landmarks.csv', delimiter=',', nrows=nRowsRead)
df1.dataframeName = 'face_landmarks.cvs'
nRow, nCol = df1.shape


print(f'There are {nRow} rows and {nCol} columns')


print()
print(df1.head(5))
