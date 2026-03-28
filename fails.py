def this_fails():
    x = 10 / 0
def this_also_fails():
    raise NameError("This is a custom name error")

try:
    this_fails()
except ZeroDivisionError as err:
    print("handling run time error:", err)
try:
    this_also_fails()
except NameError as err:
    print("handling name error:", err)