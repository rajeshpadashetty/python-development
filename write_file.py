def write_data(filename,data):
    with open(filename,'w')as file:
        file.write(data)
    print("data written successfully")
