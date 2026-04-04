with open("student.txt","r") as f1:
    data=f1.read()
    

with open("ppp.txt","w") as f:
    f.write(data)