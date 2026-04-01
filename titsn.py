import pandas as pd
titanic=pd.read_csv("titanic.csv")
print(titanic)
print("="*116)
print(titanic.head(2))
print(titanic.dtypes)
print(titanic.describe)