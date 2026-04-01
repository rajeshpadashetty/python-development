import pandas as pd
titanic=pd.read_csv("titanic.csv")
adult_name=titanic.loc[[titanic["age"]>34,"names"]]

print(adult_name.head())
