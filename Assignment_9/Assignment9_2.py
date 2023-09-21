
def display_file_contents(filename):
   try:
       with open(filename,"r") as file:
           contents = file.read()
           print("File Contents:")
           print(contents)
   except FileNotFoundError:
       print(f"The file '{filename}' does not exist.")

   except Exception as e:
       print(f"An Error occurred: {str(e)}")

if __name__ == "__main__":
    filename = input("Enter the File name:")
    display_file_contents(filename)