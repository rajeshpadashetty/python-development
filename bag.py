class BAG:
    def __init__(self):
        self.data=[]
    def add(self,x):
        self.data.append(x)
    
    def addtwice(self, x):
        self.add(x)
        self.add(x)
f1=BAG()
f1.addtwice(1)
f1.addtwice(2)
f1.addtwice(3)
f1.addtwice(4)
f1.addtwice(5)
print(f1.data)