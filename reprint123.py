import reprlib

s=reprlib.Repr()
s.maxlist=34
data=list(range(100))
print(s.repr(data))