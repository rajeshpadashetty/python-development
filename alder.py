import zlib
dat="hello world hello world hello world hello world hello world"
checksum=zlib.adler32(dat.encode())
print(checksum)

dat1=zlib.decompress(checksum.to_bytes(4, 'big'))
print(dat1)