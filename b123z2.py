import bz2
data="hello world hello world hello world hello world hello world hello world hello world hello world hello world"
compressed=bz2.compress(data.encode(),compresslevel=1)
compressed1=bz2.compress(data.encode(),compresslevel=9)
print(compressed)
print(len(compressed))
print(len(compressed1))
print(len(data))
decomp=bz2.decompress(compressed)
print(decomp.decode())