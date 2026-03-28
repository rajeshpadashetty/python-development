class negativenumbererror(Exception):
    pass
num=int(input("enter a number:"))
if num<0:
    raise negativenumbererror(("negative number not allowed"))
else:
    print("you entered:",num)