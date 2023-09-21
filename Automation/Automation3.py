from sys import *
from Arithmatic import *

def main():
    print("---------Automation Script------")
    
    print("Automation script name:",argv[0])

    if(len(argv) == 2):
       if(argv[1] == "-h" or argv[1] == "-H" ): # flag for display help
         print("This automation script is used to perform addition of two numbers")
         exit()
    
       elif(argv[1] == "-u" or argv[1] == "-U"): # flag for displaying usage of script
            print("Usage: Name_Of_Script_ first_Argument second_argument")
            print("Example:Demo.py 11 10")
            exit()
       else:
           print("There is no such option to handle")
    
    if(len(argv)!=3):
        print("Invalid number of argument")
        exit()
    else:
        Ret = Addition(int(argv[1]),int(argv[2]))
        print("Addition is:",Ret)


if __name__=="__main__":
    main()