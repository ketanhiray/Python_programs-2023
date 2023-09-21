import sys

def copy_file_content(source_filename,destination_filename):
    try:
        with open(source_filename,"r") as source_file:

            file_contents = source_file.read()


        with open(destination_filename,"w") as Dest_file:

            Dest_file.write(file_contents)


        print(f"Contents from '{source_filename}' copied to '{destination_filename}' successfully !! ")

    except FileNotFoundError:
        print("File does not exist..")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("copying")
    else:
        source_filename =sys.argv[1]
        destination_filename = sys.argv[2]
        copy_file_content(source_filename,destination_filename)

