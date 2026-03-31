from student.add import Students
def display():
    if not Students:
        print("no students found")
    else:
      print("student list:")
      for student in Students:
         print(f"Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")