while  True:
    try:
        x=int(input("please enter a number: "))
        break
    except ValueError:
        print("ohh no! that was not a  valid number.try again...")