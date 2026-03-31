def read_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print("data read successfully")
            return data
    except FileNotFoundError:
        print("file not found!")