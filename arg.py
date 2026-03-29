import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", type=int, help="first number")
    parser.add_argument("--number2", type=int, help="second number")
    parser.add_argument("--operation", choices=["add","sub","mull","div"], help="operation")
    
    args = parser.parse_args()
    
    print(args.number1)
    print(args.number2)
    print(args.operation)
    result=None
    if args.operation=="add":
        result=args.number1+args.number2
    elif args.operation=="sub":
        result=args.number1-args.number2
    elif args.operation=="mull":
        result=args.number1*args.number2
    elif args.operation=="div":
        result=args.number1/args.number2
else:
        print("unsupported operation")
 
print("result=",result)