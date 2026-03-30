import time
start=time.time()
for i in range(1000000):
    if i==10000:
     print(i ,end="")
     break

end = time.time()
print("time taken to execute the loop is ",end-start)