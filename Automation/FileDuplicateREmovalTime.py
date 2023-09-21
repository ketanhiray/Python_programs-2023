from sys import*
import os
import hashlib
import time

def DeleteFiles(dict1):
    results = list(filter(lambda x : len (x)>1,dict1.values()))
    
    icnt = 0
    if len(results)> 0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    os.remove(subresult)
            
            icnt = 0 
    
    else:
        print("No duplicate files found.")


def hashfile(path,blocksize=1024):
    afile =open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    
    while len(buf)>0:
        hasher.update(buf)
        buf =afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def FindDuplicate(path):
    flag =os.path.isabs(path)
    
    if flag == False:
        path = os.path.abspath(path)

    exits = os.path.isdir(path)

    dups ={}
    if exits:
        for dirName,subdirs,fileList in os.walk(path):
            print("Current folder is:"+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                
                if file_hash in dups:
                   dups[file_hash].append(path)
                
                else:
                    dups[file_hash] = [path]
        
        return dups
    else:
             print("Invalid path")
def PrintResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results)>0:
        print("Duplicates found:")

        print("The following files are identical")

        icnt = 0;
        for result in results:
            for subresult in result:
               icnt +=1
               if icnt >=2 :
                   print('\t\t%s'% subresult)

    else:
        print("No Duplicate Files found.")             

     
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
       arr ={}
       startTime = time.time()
       arr = FindDuplicate(argv[1])
       PrintResults(arr)
       DeleteFiles(arr)
       endTime = time.time()

       print('Took %s seconds to evaluate.'%(endTime -startTime))
    
    except ValueError:
        print("Erro: Invalid datatype of input")
    
    except Exception as E:
        print("Error : Invalid input",E)


if __name__ == "__main__":
    main()