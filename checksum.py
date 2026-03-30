import zlib
data="hello world hello world hello world hello world hello world hello world hello world hello world hello worldd hello world"
checksum=zlib.crc32(data.encode())
print(checksum)