import pandas as pd
#student attendance system with roll number
data={
    "name":["ram","raj","ravi","ragava"],
    "roll_number":[123,1234,12345,123456],
    "attandance":["80%","90%","95%","70%"]    
}
df=pd.DataFrame(data)
df["result"]=["pass","pass","fail","pass"]
print(df)
new_rec=pd.DataFrame({
    "name":["arvind","fayaz"],
    "roll_number":[123456,1234567],
    "attandance":["85","92"],
    "result":["pass","pass"]
})
result=pd.concat([df, new_rec])
print(result)