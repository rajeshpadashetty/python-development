from student.add import Students
def delete(name):
    for stu in Students:
        if stu["name"]==name:
            Students.remove(stu)
            print("deleted successfully")
            return
    print("Student not found!")