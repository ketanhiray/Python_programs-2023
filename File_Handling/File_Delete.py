import os.path

def main():
    print("Enter the name of the file you want to create :")
    File_name = input()

    if os.path.exists(File_name):
       os.remove(File_name)
    else:

        print("There is no such file")
    

if __name__ =="__main__":
    main()
