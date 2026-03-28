class ageerror(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"invalid age: {self.age}")
age=-18
try:
    if age<0:
        raise ageerror(age)
except ageerror as e:
    print("valid age:",e.age)