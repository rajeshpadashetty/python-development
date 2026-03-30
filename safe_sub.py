from string import Template
t=Template("my name is $name and i am $age years old")
print(t.safe_substitute(name="rajesh"))