import pandas as pd

data = {
    "name": ["Raj", "Sam", None],
    "age": [20, None, 25]
}

df = pd.DataFrame(data)

print(df.notna())