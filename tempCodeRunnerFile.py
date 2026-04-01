import pandas as pd

data={
    "name":["rajesh","gangdhar","padashetty","jagannath"],
    "age":[21,22,44,90]
}

df=pd.DataFrame(data,index=["member1","member2","member3","member4"])
print(df)
print(df.loc["member1"])
print(df.loc["member2"])
print(df.loc["member3"])
print(df.loc["member4"])

print(df.iloc[0])
df["job"]=["python developer","java developer","N/A","C++ DEVELOPER"]
print(df)
ADD_NEW=pd.DataFrame([{"name":"rag