def ResultDay(RESULT):
    match RESULT:
        case "monday":
            print("Monday")
        case "tuesday":
            print("Tuesday")
        case "wednesday":
            print("Wednesday")
        case "thursday":
            print("Thursday")
        case "friday":
            print("Friday")
        case _:
            print("Invalid day")

tt=ResultDay("monday")
print(tt)