import pandas as pd

data = {
    "Order_ID": [101,102,103,104,105,106,107,108],
    "Customer": ["Ram","Raj","Ravi","Rani","Ramesh","Raj","Ram","Rani"],
    "Product": ["Laptop","Mobile","Laptop","Tablet","Mobile","Laptop","Tablet","Mobile"],
    "Category": ["Electronics"]*8,
    "Quantity": [1,2,1,3,2,1,2,1],
    "Price": [50000,20000,50000,15000,20000,50000,15000,20000],
    "Order_Date": ["2026-01-10","2026-01-12","2026-02-05","2026-02-20",
                   "2026-03-01","2026-03-15","2026-03-18","2026-04-01"]
}

df = pd.DataFrame(data)


df["Order_Date"] = pd.to_datetime(df["Order_Date"])


df["Total_Price"] = df["Quantity"] * df["Price"]

print(df)


print("Total Sales:", df["Total_Price"].sum())
print("Minimum Sales:", df["Total_Price"].min())
print("Maximum Sales:", df["Total_Price"].max())
print("Total number of sales:", df["Quantity"].count())


print("\nSales price greater than 5000:")
print(df[df["Price"] > 5000][["Order_ID","Product","Price"]])


print("\nTop Selling Product:")
print(df.groupby("Product")["Quantity"].sum().sort_values(ascending=False))

df["Month"] = df["Order_Date"].dt.month
print("\nMonthly Sales:")
print(df.groupby("Month")["Total_Price"].sum())


#most Ordered Catagory
print(df.groupby("Category")["Quantity"].sum())
print(df.groupby("Category")["Quantity"].sum())


#average Order value
print("average Order value:",df["Total_Price"].mean())

#top three highest values
print(df.sort_values(by="Price", ascending=False).head(3))
