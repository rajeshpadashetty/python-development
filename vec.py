vec=[2,-4,-6,6,8,4,8,10]
print(vec)
vec1=[x*2 for x in vec]
print(vec1)

vec3=[x for x in vec if x>=0]
print(vec3)
vec4=[abs(x) for x in vec]
print(vec4)\
freshfruit=["apple   ","banana   ","mango   ","papaya    "]
print(freshfruit)
vec=[wep.strip() for wep in freshfruit]
print(vec)
x=[3,4,5]
y=[6,8,2]
sn=[(i,j**2) for i in x for j in y]