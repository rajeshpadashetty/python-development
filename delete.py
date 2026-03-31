from.add import employee
def dellete():
    for emp in employee:
        if emp["id"]==id:
            employee.remove(emp)
            print("employee deleted succssfully")
            return
        print("employee not found")
