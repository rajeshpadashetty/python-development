from .add import employee

def veiw_emp():
    if not employee():
        print("no one employee is found")
    else:
        for emp in employee:
            print(f"id:{emp[id]},name:{emp["name"]},salary:{emp["salary"]},rolr:{emp["role"]}")

    