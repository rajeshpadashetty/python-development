
from student.add import add
from student.dis import display
from student.deletel import delete

print("\n Welcome to student Management system")
print("\n--- Student Management System ---")
print("1. Add Student")
print("2. Delete Student")
print("3. Display Students")
print("4. Exit")
choice = input("enter your choice")
if choice == "1":
    name = input("enter student name")
    age = int(input("enter student age"))
    course = input("enter the course")
    add(name, age, course)
elif choice == "2":
    name = input("enter student name to delete")
    delete(name)
elif choice == "3":
    display()
elif choice == "4":
    print("existing from the system")
    exit()
else:
    print("invalid choice")


