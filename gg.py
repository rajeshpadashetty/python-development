import pandas as pd
data1=[30.40,50,60,70,80,111]
series1=pd.Series(data1,index=["a","b","c","d","e","f"])
print(series1)
print([series1>=100])
