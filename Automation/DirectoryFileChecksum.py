from sys import*
import os
import hashlib


def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    
    buf = afile.read(blocksize)
    
    while len(buf)>0:
        hasher.update(buf)
        buf =afile.read(blocksize)
        
    afile.close()
    return hasher.hexdigest()

def DisplayChecksum(path):
    flag =os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exits = os.path.isdir(path)
    if exits:
        for dirName,subdirs,fileList in os.walk(path):
            print("Current folder is:"+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print('')
    else:
        print("Invalid path")
def main():
    print("-------Marvellous Infosystems by Piyush khairnar------")
    
    print("Application Name:" +argv[0])

    if(len(argv) != 2):
        print("Error:Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to traverse specific directory")
        exit()


    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage: ApplicationName AbsolutePath_ of Directory")
        exit()

    try:
        
        #DirectoryWatcher(argv[1])
        arr = DisplayChecksum(argv[1])
    
    except ValueError:
        print("Erro: Invalid datatype of input")
    
    except Exception as E:
        print("Error : Invalid input",E)


if __name__ == "__main__":
    main()