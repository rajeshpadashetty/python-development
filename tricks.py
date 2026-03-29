class dog:
   
   tricks=[]
   def __init__(self,name):
         self.name=name
   def add_tricks(self,trick):
        self.tricks.append(trick)
d=dog("tommy")
d.add_tricks("roll over")
d.add_tricks("play dead")
print(d.tricks)
