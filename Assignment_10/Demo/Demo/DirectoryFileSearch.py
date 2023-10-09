import os
import sys
import logging

def display_files(directory,file_extension):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")
        
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory")
        
        for filename in os.listdir(directory):
            if filename.endswith(file_extension):
                logging.info(f"Found file: {os.path.join(directory,filename)}")

        
    except FileNotFoundError as e:
        logging.error(f"Error: {e}")
    
    except NotADirectoryError as e:
        logging.error(f"Error: {e}")

    except Exception as e:
        logging.error(f"An unexpected error occurred :{e}")

def main():
    logging.basicConfig(filename= 'logfile.log', level= logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s ')

    try:
        if len(sys.argv)!=3:
            raise ValueError("Usage: DirectoryFileSearch.py <directory> <file_extension>")

        directory =sys.argv[1]
        file_extension =sys.argv[2]

        if not file_extension.startswith("."):
            raise ValueError("File extension should start with '.'")

        display_files(directory,file_extension)

    except ValueError as e:
        logging.error(f"Error : {e}")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()    


#Python DirectoryFileSearch.py "c:\Users\khiray\OneDrive\Documents\Python\My_Programs\Python_programs\Assignment_10\Demo" ".txt" 