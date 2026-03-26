cube=[]
for i in range(1,20):
    if(i%2==0):
        cube.append(i**3)
        print(cube)
#short form or list comprehenstion  of list in python
cube=[i**3 for i in range(1,20) if i%2==0 ]
print(cube)
#using map lamada function in python
cube=list(map(lambda x: x**3, range(1,20)))
print(cube)