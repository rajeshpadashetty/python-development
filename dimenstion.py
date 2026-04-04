import numpy as np

array = np.array([
    [['A','B','C'], [1,2,3], ['a','b','c']],
    [['E','F','G'], [5,6,7], ['e','f','g']],
    [['I','J','K'], [9,10,11], ['i','j','k']]
])

print(array.ndim)
print(array.shape)
print(array[1,1,1])