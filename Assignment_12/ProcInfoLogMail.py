import psutil
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sys import argv
from email import encoders
from email.mime.base import MIMEBase


def get_process_info():

    process_info =[]
    for process in psutil.process_iter(['pid','name','username']):
        try:
            process_info.append((process.info['name'], process.info['pid'], process.info['username']))
        
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return process_info

def create_log_file(directory,process_info):
    log_file_path = os.path.join(directory,"ProcessInfoLog4.txt")

    with open(log_file_path,'w') as log_file:
        log_file.write("Process Name\tPID\tUsername\n")
        for name,pid,username in process_info:
            log_file.write(f"{name}\t{pid}\t{username}\n")
    return log_file_path
    
def send_email(toaddr,log_file_path):
    try:
        fromaddr = "ketanpython7@gmail.com"
        #toaddr = "ketanhiraypatil@gmail.com"
        password = "blkphqgsbjmfqexf"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = f"""
        Hello {toaddr}
        Welcome
        Please find attachment document which contains the log of Running Process.

        Log file is created as: {log_file_path}

        This is an Auto-generated mail.

        Thanks,
        Ketan
        """

        subject = f"Marvellous Infosystems Process log generated "
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        attachment = open(log_file_path, "rb")  # binary

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        #part.add_header('Content-Disposition', f"attachment; filename={filename}")
        part.add_header('Content-Disposition', 'attachment' , filename=os.path.basename(log_file_path))
        msg.attach(part)

        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(fromaddr, password)
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)

        print("Log file successfully sent through Mail")

    except Exception as e:
        print("Unable to send mail", e)



    
def main():
    directory_name = input("Enter the Directory name:")
    email_address = input("Enter the email address:")
   
    if not os.path.exists(directory_name):
        os.makedir(directory_name)
    
    process_info =get_process_info()
   
    log_file_path = create_log_file(directory_name,process_info)

    send_email(email_address,log_file_path)

    print(f"Process infomation has been logged to {log_file_path} and sent to {email_address}")


if __name__ == "__main__":
    main()

