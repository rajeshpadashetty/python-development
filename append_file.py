def append_data(filename, data):
    with open(filename, 'a') as f:
        f.write(data)
    print("Data appended successfully")