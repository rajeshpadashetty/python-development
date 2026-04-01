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
t1=type(df["age"])
print(t1)
t2=df["age"].shape
print(t2)
t4=type(df[["age","sex"]])
print(t4)
t5=df[["age","sex"]].shape
print(t5)