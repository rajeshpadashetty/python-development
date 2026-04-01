import pandas as pd

df = pd.read_csv("data.csv",index_col=Name)
print(df.to_string(index=False))
print(df.loc("name"))
