import os.path

def main():
    print("Enter the name of the file you want to create :")
    File_name = input()

    if os.path.exists(File_name):
        print("Unable to create file as file is already existing")
    else:

        fobj = open(File_name,"x")
    

if __name__ =="__main__":
    main()
