def ADDDETAILS():
    f=open("student.txt","a")
    name=input("enter your name")
    age=int(input("enter your age"))
    Marks=int(input("enter the marks"))
    f.write(name + "," +str(age)+","+str(Marks)+"\n")
    f.close()

def VEIWDETAILS():
      f=open("student.txt","r")
      print(f.read())
      f.close()

print("plz enter 1(one) for adding details")
print("plz enter 2(two) for to veiw details")

choice=int(input("enter youe choice"))

if choice==1:
      print("thank you for intrested to adding dertails")
      ADDDETAILS()

elif choice==2:
      print("thankyou for veiwing the details")
      VEIWDETAILS()
      
else:
    exit()


