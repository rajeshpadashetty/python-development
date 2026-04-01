import pandas as pd

data={
    "EMP_NAME":["EMP1","EMP2","EMP3","EMP4","EMP5"],
    "EMP_ID":["EMP123","EMP1234","EMP12345","EMP123456","EMP1234567"],
    "EMP_C_NAME":["IBM","MICROSOFT","AMEZON","NVIDIA","FLIPCART"]
}
dataframe=pd.DataFrame(data,index=["SL1","SL2","SL3","SL4","SL5"])
dataframe["salary"]=["1.00.000","2.00.000","3,00,000","4,00,000","5,00,000"]
print(dataframe)
data1={
    "EMP_NAME":["EMP6"],
    "EMP_ID":["EMP12345678"],
    "EMP_C_NAME":["APPLE"],
    "salary":["6,00,000"]
}
ADD_NEW=pd.DataFrame(data1)
result = pd.concat([dataframe, ADD_NEW])
print(result)
