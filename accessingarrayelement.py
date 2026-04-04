import numpy as np

array = np.array([
    [['A','B','C'], [1,2,3], ['a','b','c']],
    [['E','F','G'], [5,6,7], ['e','f','g']],
    [['I','J','K'], [9,10,11], ['i','j','k']]
])

world=array[0,0,0]+array[2,2,2]+array[1,2,0]+array[2,1,0]
print(world)