class  lamorgini1:
    def lamorgini1(self):
        print("lambargini color is black")
        print("fastest car in the world")
class odi(lamorgini1):
    def odi1(self):
        print("odi color is white")
        print("odi is the second fastest car in the world")
class ferrari(odi,lamorgini1):
    def ferrarii(self):
        print("ferrari color is red")
        print("ferrari is the third fastest car in the world")


a1=lamorgini1()
print(a1.lamorgini1())
a2=odi()
print(a2.odi1())
a3=ferrari()
print(a3.ferrarii())
print(a3.lamorgini1())
print(a3.odi1())