import os

def main():
    print("Enter the name of the file that you want to open for writting purpose :")
    File_name = input()

    if os.path.exists(File_name):
       fobj = open(File_name,"a") # append mode
       if fobj:
             print("File successfully opened in append mode")
             
             print("Enter data that you want to write in file:")
             Data = input()

             fobj.write(Data) # write data into file
             fobj.close()
       else:
           print("Unable to opne file")
    
    else:

        print("There is no such file")
    

if __name__ =="__main__":
    main()
