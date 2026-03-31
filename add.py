employee=[]
def employee(name,id,salary,role,company_name):
  emp={
    "name":name,
    "id":id,
    "salary":salary,
    "role":role,
    "company_name":company_name
  }
  employee.append(emp)
  print("employee details added succesfully")