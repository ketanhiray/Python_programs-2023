import os

def check_file_exist(filename):
    if os.path.exists(filename):

        print(f"File '{filename}' exist ")

    else:
        print(f"File '{filename}' Not Exist")


if __name__ == "__main__":
    filename = input("Enter the File name:")
    check_file_exist(filename)