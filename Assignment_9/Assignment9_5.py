def counting_String(filename,target_string):
    try:
        with open(filename,"r") as file:
            data = file.read()
            frequency = data.count(target_string)
            return frequency
    except FileNotFoundError:
        print("Error !! File does not exist..")
    except Exception as e:
        print(f"An error occurred : {str(e)}")

if __name__ == "__main__":
    filename = input("Enter file name:")
    target_string =input("Enter string to count:")
    
    frequency = counting_String(filename, target_string)
    if frequency is not None:
        print(f"The frequency of '{target_string}' in '{filename}' is {frequency}.")