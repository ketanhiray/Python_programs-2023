import sys

def compare_files(file1,file2):
    try:
        with open(file1,"r") as f1, open(file2,"r") as f2:
            data1 = f1.read()
            data2 = f2.read()
            if data1 == data2:
                print("Success: Both files have the same Contents..")
            else:
                print("Failue : Both files have the different Contents..")

    except FileNotFoundError:
        print("Error !! File does not exist..")
    except Exception as e:
        print(f"An error occurred : {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Compairing")
    else:
        file1 =sys.argv[1]
        file2 = sys.argv[2]
        compare_files(file1,file2)