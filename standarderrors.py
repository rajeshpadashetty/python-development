import sys

sys.stdout.write("hello world")
sys.stderr.write("error message\n")
print("this is a new type of error",file=sys.stderr)
print(input())
print(sys.stdin.read())