import os
def delete_data(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("file deleted successfully")
    else:
        print("file not found!")