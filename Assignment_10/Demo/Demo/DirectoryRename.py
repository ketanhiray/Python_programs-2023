import os
import sys
import logging

def rename_files(directory,old_extension,new_extension):
    try:

        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")
        
        if not os.path.isdir(directory):
            raise NotADirectoryError(f" '{directory}' is not a directory.")
        
        for filename in os.listdir(directory):
            if filename.endswith(old_extension):
                old_file_path = os.path.join(directory,filename)
                new_filename = os.path.splitext(filename)[0] + new_extension
                new_file_path = os.path.join(directory,new_filename)

                os.rename(old_file_path, new_file_path)
                logging.info(f"Renamed file: {old_file_path} to {new_file_path} ")


    except FileNotFoundError as e:
        logging.error(f"Error: {e}")
    
    except NotADirectoryError as e:
         logging.error(f"Error: {e}")

    except Exception as e:
        logging.error(f"An Unexpected error occured: {e}")


def main():
    logging.basicConfig(filename='logfile.log',level=logging.INFO,format='%(asctime)s - %(message)s')


    try:
        if len(sys.argv) != 4:
            raise ValueError("Usage:DirectoryRename.py <directory> <old_extension> <new_extension>")
            
        directory = sys.argv[1]
        old_extension = sys.argv[2]
        new_extension = sys.argv[3]
        if not old_extension.startswith(".") or not new_extension.startswith("."):
                raise ValueError("File extension should start")
        

        rename_files(directory, old_extension,new_extension)

    except ValueError as e:
        logging.error(f"Error: {e}")
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ =="__main__":
    main()