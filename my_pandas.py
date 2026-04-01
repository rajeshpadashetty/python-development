import pandas as pd

df=pd.DataFrame(
        {
    "name":[
        "rajesh",
        "ramesh",
        "rakesh"
         ],
    "age":[21,32,44],
    "sex":["male","male","male"]
        }
    )
print(df)

print(df["age"].max())
print(df["age"].min())
print(df.describe())

