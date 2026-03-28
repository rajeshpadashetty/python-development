import sys

try:
   with open('myfile.txt') as f:
    s = f.read()
    i=s.strip()

except OSError as err:
    print("OS error:",err)
except ValueError:
    print("could not convert data into intreger.")
except Exception as err:
    print(f"unexpectes error:{err=},{type(err)=}")
    raise
