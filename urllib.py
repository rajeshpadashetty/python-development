from urllib.request import urlopen

with urlopen('http://www.python.org') as response:
    for line in response:
        line = line.decode()
        if 'updated' in line:
            print(line.strip())
