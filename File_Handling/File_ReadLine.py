import os
#File read line 
def main():
    print("Enter the name of the file that you want to open for Reading purpose :")
    File_name = input()

    if os.path.exists(File_name):
       fobj = open(File_name,"r") # reading mode
       if fobj:
             print("File successfully opened in read mode")
             
             Line1 =fobj.readline()
             Line2 =fobj.readline()
             Line3 =fobj.readline()

             print("first line is:",Line1)
             print("second line is:",Line2)
             print("third line is:",Line3)
            
             fobj.close()
       else:
           print("Unable to opne file")
    
    else:

        print("There is no such file")
    

if __name__ =="__main__":
    main()
