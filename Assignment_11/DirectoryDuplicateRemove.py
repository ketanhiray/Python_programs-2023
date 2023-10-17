import os
import sys
import hashlib



def get_file_checksum(file_path,block_size = 65536):
    hasher = hashlib.md5()
    with open(file_path,'rb') as file:
        buf = file.read(block_size)
        while len(buf)>0:

             hasher.update(buf)
             buf =file.read(block_size)
    
    return hasher.hexdigest()


def find_duplicate_files(directory):
    file_checksums ={}
    duplicate_files =[]

    for foldername, subfolder,filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername,filename)
            checksum = get_file_checksum(file_path)

            if checksum in file_checksums:
                duplicate_files.append((file_path,file_checksums[checksum]))

            else:

                file_checksums[checksum]= file_path


    return duplicate_files

def delete_diplicate_files(duplicate_files):
    for file_pair in duplicate_files:
        print(f"Deleting duplicate file: {file_pair[0]}")
        os.remove(file_pair[0])


def write_to_log(duplicate_files):
    with open("log3.text","w") as log_file:
        if duplicate_files:
            log_file.write("Deleted Duplicate files :\n")
            for file_pair in duplicate_files:
                log_file.write(f"{file_pair[0]}\n{file_pair[1]}\n\n")
        
        else:
            log_file.write("No duplicate files are found!!")

if __name__=="__main__":
    if len(sys.argv)!= 2:
        print("Usage: Python DirectoryDuplicate.py <directory>")
    
    else:

        directory_name =sys.argv[1]
        if os.path.exists(directory_name):
            duplicate_files = find_duplicate_files(directory_name)
            delete_diplicate_files(duplicate_files)
            write_to_log(duplicate_files)
            print("Duplicate files delted and logged in Log3.txt")
        else:
            print(f"The specified directory '{directory_name}' does not exist.")



