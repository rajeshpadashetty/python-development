import pandas as pd

df=pd.DataFrame(
        {
    "name":[
        "rajesh",
        "ramesh",
        "rakesh",
        "ragava",
        "raventh",
        "tarun"
         ],
    "age":[21,32,44,66,77,88],
    "sex":["male","male","male","male","male","male",]
        }
    )
filter=df[df["age"]>30]
t1=filter.head()
print(t1)
print(df["age"]>30)

