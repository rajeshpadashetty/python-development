str="www.googl.com"
print(str.upper())
str1="straße"
print(str1.casefold())
print(str.center(20),"_")
print(str.encode())
print(str.encode().decode())
print(str.endswith("com"))
print(str.startswith("www"))
print(str.find("google"))
print(str.removesuffix(".com"))
print(str.removeprefix("www."))
print("the sum of two numbers is : {0}".format(2+3))
print("{name}".format_map({"name": "Raj"}))
print('-'.join("python"))
print("python".ljust(10),'-')
mk=str.maketrans("abc","xyz")
table="apple, banana ,cat,cammal,animal".translate(mk)
print(table)
print("rajesh padasetty".partition(" "))

for i in range(5):
    print(i)
for i in range(5):
    for j in range(5):
        print("sexy ",end="")
    print()
