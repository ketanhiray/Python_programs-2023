from sys import *
import os
import time

def DirectoryTravel(DirName):
     print("We are going to scan the Directory:",DirName)
     
     flag =os.path.isabs(DirName)

     if flag == False:
          DirName = os.path.abspath(DirName)# absolute path conversion

     exist = os.path.isdir(DirName)

     if exist:
          for foldername,subfoldername,filename in os.walk(DirName) :
               print("Current Directory name:",foldername)

               for subname in subfoldername:
                print("Subfolder name is :",subname)
             
               for fname in filename:
                   print(fname,":",os.path.getsize(os.path.abspath(fname)))
                    #print(os.path.abspath(fname))
     else:
          print("Invalid path")     

def main():
    print("---------Automation Script------")
    
    print("Automation script name:",argv[0])
    
    if(len(argv)!=2):
        print("Invalid number of argument")
        exit()
   
   
    if(argv[1] == "-h" or argv[1] == "-H" ): # flag for display help
         print("This automation script is used to perform File Automation")
         exit()
    
    elif(argv[1] == "-u" or argv[1] == "-U"): # flag for displaying usage of script
            print("Usage: Name_Of_Script_ first_Argument")
            print("Example:Demo.py Marvellous")
            exit()
    else:
          #Logic
        starttime= time.time()
        DirectoryTravel(argv[1])
        endtime= time.time()
        #os.path.getsize()
        print("The script took to execute as:",endtime-starttime)
    
      


if __name__=="__main__":
    main()


#path = any
#python3 filename.py "marvellous"