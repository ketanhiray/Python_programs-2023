import os
import sys
import shutil
import logging


def copy_files_with_extension(source_directory,destination_directory,file_extension):
    try:

        if not os.pth.exists(source_directory):
            raise FileNotFoundError(f"Source directory '{source_directory}' not found.")
        
        if not os.path.isdir(source_directory):
            raise NotADirectoryError(f"'{source_directory}' is not a directory.")
        
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
            logging.info(f"Created destination directory: {destination_directory}")
        
        for filename in os.listdir(source_directory):
            if filename.endswith(file_extension):
                source_file_path =os.path.join(source_directory,filename)
                destination_file_path =os.path.join(destination_directory,filename)

                shutil.copy2(source_file_path,destination_file_path)
                logging.info(f"Copied file: {source_file_path} to {destination_file_path}")
    
    except FileNotFoundError as e:
        logging.error(f"Error: {e}")
    
    except NotADirectoryError as e:
        logging.error(f"Error: {e}")
    
    except Exception as e:
        logging.error(f"An unexpected error occured : {e}")


def main():

    logging.basicConfig(filename='Loginfile1.log',level=logging.INFO,format='%(asctime)s - %(levelname)s : %(message)s')\
    
    try:
        if len(sys.argv) !=4:
            raise ValueError("Usage : DirectoryCopyExt.py <source_directory> <destination_directory><file_extention>")
        
        source_directory =sys.argv[1]
        destination_directory =sys.argv[2]
        file_extension =sys.argv[3]

        if not file_extension.startswith("."):
            raise ValueError("file extension should start with '.'")
        
        copy_files_with_extension(source_directory, destination_directory, file_extension)

    except ValueError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
