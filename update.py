from .add import employee

def update(name,id,salary,role,company_name):
    for emp in employee:
        if emp[id]==id:
            emp[name]==name,
            emp[salary]==salary
            emp[role]==role
            emp[company_name]==company_name
            print("Employee updated successfully!")
            return
    print("Employee not found.")

