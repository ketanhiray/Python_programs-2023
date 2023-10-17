import os
import hashlib
import logging
import sys

def calculate_checksum(file_path):

    hasher = hashlib.md5()
    with open(file_path, "rb") as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    
    return hasher.hexdigest()

def directory_checksum(directory):

    checksums ={}

    try:

        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f))]

        for file_name in files:
            file_path = os.path.join(directory,file_name)

            try:

                checksum = calculate_checksum(file_path)
                checksums[file_name] = checksum
                logging.info(f"Checksum of {file_name}:{checksum}")
            
            except Exception as e:
                logging.error(f"Error calculating checksum for{file_name}:{str(e)}")
    
    except Exception as e:
        logging.error(f"Error listing files in the directory :{str(e)}")
    
    return checksums

def setup_logging(log_file):

    logging.basicConfig(filename=log_file,level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s",)

def main():
    if len(sys.argv) != 2:
        print("Usage: python DirectoryChecksum.py <drectory_name>")
        sys.exit(1)

    
    directory_name =sys.argv[1]
    log_file = "checksum_log.txt"

    setup_logging(log_file)

    try:
        if not os.path.exists(directory_name) or not os.path.isdir(directory_name):
            logging.error("Invaild directory path. plese enter the valif path")

            sys.exit(1)

        logging.info(f"Calculating checksum of files in directory: {directory_name} ")

        checksums = directory_checksum(directory_name)
        logging.info("Checksum calculation complated.")
    
    except Exception as e:
        logging.error(f"An unexpected error occuted:{str(e)}")

        sys.exit(1)

if __name__ == "__main__":
    main()