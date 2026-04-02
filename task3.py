import pandas as pd

data = {
    "Order_ID": [101,102,103,104,105,106,107,108,109,110],
    "Date": [
        "2026-01-01","2026-01-02","2026-01-03","2026-01-04","2026-01-05",
        "2026-01-06","2026-01-07","2026-01-08","2026-01-09","2026-01-10"
    ],
    "Product": [
        "Laptop","Mobile","Tablet","Laptop","Mobile",
        "Tablet","Laptop","Mobile","Tablet","Laptop"
    ],
    "Category": [
        "Electronics","Electronics","Electronics","Electronics","Electronics",
        "Electronics","Electronics","Electronics","Electronics","Electronics"
    ],
    "Region": [
        "North","South","East","West","North",
        "South","East","West","North","South"
    ],
   "Sales_Amount": [50000,20000,15000,55000,22000,16000,52000,21000,14000,58000],
    "Quantity": [2,5,3,2,6,4,2,5,3,2],
    "Customer_Type": [
        "Regular","New","Regular","New","Regular",
        "New","Regular","New","Regular","New"
    ]
}

df = pd.DataFrame(data)


print(df)
df.to_excel("ABC.xlsx", sheet_name="passengers", index=False)
df.to_csv("sales.csv")
df.to_csv("sales.json")
print(df.groupby("Sales_Amount").min())
print(df.groupby("Quantity").sum())
print(df.groupby("Sales_Amount").count())

