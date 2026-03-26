def rangepointer(point):
    match point:
        case (0,0):
            print("origin")
        case (0,y):
            print(f"y={y}")
        case (x,0):
            print(f"x={x}")
        case (x,y):
             print(f"x={x},y={y}")


        case _:
         raise ValueError("Not a point")
        

rangepointer((0,1))