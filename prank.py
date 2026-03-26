vec=[[1,2,3],[2,4,6],[8,10,12]]
print(vec)
vec1=[num for i in vec for num in i]
print(vec1)

from math import pi

from numpy import matrix
tender=[str(round(pi,i)) for i in range(1,5)]
print(tender)
trailer=[[row[i] for row in matrix] for i in range(4)]

print(trailer)