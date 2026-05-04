import numpy as np
a=np.arange(10)**3
print(a)
print(a[2:8])
a[:6:2] = 1000
print(a)
print(a[::-1])