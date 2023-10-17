import psutil
import sys
import logging
from datetime import datetime


def get_process_info(process_name):
    process_info =[]
    for process in psutil.process_iter(['pid','name','username']):
        process_info.append((process.info['name'], process.info['pid'],process.info['username']))
    return process_info

def display_process_info(process_info):
    for process in process_info:
        logging.info(f"Name:{process[0]}, PID: {process[1]}, Username:{process[2]}")


def log_message(message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{current_time}] {message}"
    logging.info(log_entry)


if __name__ == "__main__":

    logging.basicConfig(filename='ProcInfoLog2.txt', level=logging.INFO)

    try:

        if len(sys.argv) != 2:
            raise ValueError("Usage: Python ProcInfo2.py <process_name>")
        
        process_name = sys.argv[1]

        process_info = get_process_info(process_name)
       
        if not process_info:
            log_message(f"No Running Process found with Name '{process_name}'!!")
        
        else:
             display_process_info(process_info)
             log_message(f"Process infomation for '{process_name}' displayed sucessfully!!!")

    
    except Exception as e:
        log_message(f"Error: {str(e)}")

    
    finally:
        logging.shutdown()
        

