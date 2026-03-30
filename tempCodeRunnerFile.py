from timeit import time
print(Timer("t=a;a=b;b=t","a=1; b=2").timeit())

