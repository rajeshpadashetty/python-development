import gzip
data="hello world hello world hell world hello world hello world hello world hello world hello world hello world hello world"
compressed=gzip.compress(data.encode(),compresslevel=1)
print(data)
print(compressed)
compressed1=gzip.compress(data.encode(),compresslevel=9)
print(compressed1)
print(len(compressed))
print(len(compressed1))
print(len(data))