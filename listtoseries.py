import pandas as pd
data=[2,4,6,8,10]
series=pd.Series(data)
print(data)
data1=(1,3,4,5,6,7,8,9,10,11)
series1=pd.Series(data1,index=["a","b","c","d","e","f","g","h","i")
print(series1)
data2=("ram","raj","ravi","randi")
series2=pd.Series(data2)
print(series2)
