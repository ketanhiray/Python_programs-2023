import psutil
import os


def get_process_info():

    process_info =[]
    for process in psutil.process_iter(['pid','name','username']):
        try:
            process_info.append((process.info['name'], process.info['pid'], process.info['username']))
        
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return process_info


def main():
    directrory_name = input("Enter the Directory name:")
   
    if not os.path.exists(directrory_name):
        os.makedir(directrory_name)
    
    process_info =get_process_info()

    log_file_path = os.path.join(directrory_name,"ProcessInfoLog3.txt")

    with open(log_file_path,'w') as log_file:
        log_file.write("Process Name\tPID\tUsername\n")
        for name,pid,username in process_info:
            log_file.write(f"{name}\t{pid}\t{username}\n")

    
    print(f"Process infomation has been logged to {log_file_path}")


if __name__ == "__main__":
    main()

