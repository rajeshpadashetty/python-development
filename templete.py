from string import Template

t=Template("my name is $name and i am $age years old")
print(t.substitute(name="rajesh",age=18))
