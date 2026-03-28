try:
    raise NameError("This is a name error!")
except NameError as err:
    print("handling name error:", err) 