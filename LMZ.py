import lzma

data = b"Hello Hello Hello Hello"

compressed = lzma.compress(data)
print(compressed)
