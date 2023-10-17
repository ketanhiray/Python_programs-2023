import os
import time
import psutil
import urllib.request
import smtplib
import schedule
from sys import argv
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib.request.urlopen("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox", timeout=1)
        return True
    except urllib.URLError as err:
        return False

def mail_sender(filename, timestamp):
    try:
        fromaddr = "ketanpython7@gmail.com"
        toaddr = "ketanhiraypatil@gmail.com"
        password = "blkphqgsbjmfqexf"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = f"""
        Hello {toaddr}
        Welcome
        Please find attachment document which contains the log of Running Process.

        Log file is created as: {filename}

        This is an Auto-generated mail.

        Thanks,
        Ketan
        """

        subject = f"Marvellous Infosystems Process log generated at: {timestamp}"
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filename, "rb")  # binary

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename={filename}")
        msg.attach(part)

        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(fromaddr, password)
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)

        print("Log file successfully sent through Mail")

    except Exception as e:
        print("Unable to send mail", e)

def process_log(log_dir='Marvellous'):
    list_processes = []

    if not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir)
        except OSError as e:
            print(f"Error creating directory: {e}")

    separator = "-" * 80

    log_path = os.path.join(log_dir, f"MarvellousLog_{time.strftime('%Y%m%d%H%M%S')}.log")

    try:
        with open(log_path, 'w') as f:
            f.write(separator + "\n")
            f.write("Marvellous Infosystem Process Logger: " + time.ctime() + "\n")
            f.write(separator + "\n")
            f.write("\n")

            for proc in psutil.process_iter():
                try:
                    pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
                    vms = proc.memory_info().vms / (1024 * 1024)
                    pinfo['vms'] = vms
                    list_processes.append(pinfo)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            for element in list_processes:
                f.write("%s\n" % element)

        print("Log file is successfully generated at location", log_path)

        connected = is_connected()

        if connected:
            start_time = time.time()
            mail_sender(log_path, time.ctime())
            end_time = time.time()

            print(f'Took {end_time - start_time} seconds to send mail')

        else:
            print("There is no internet connection")

    except Exception as e:
        print(f"Error processing log: {e}")

def main():
    print("---- Marvellous Infosystem by piyush kahirnar----")
    print("Application name:", argv[0])

    if len(argv) != 2:
        print("Error: Invalid number of arguments")
        exit()

    if argv[1] == "-h" or argv[1] == "-H":
        print("This automation script is used for recording logs of running processes")
        exit()

    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage: python script.py AbsolutePath_of_directory")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(process_log)
        while True:
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception as e:
        print("Error: Invalid input", e)

if __name__ == "__main__":
    main()


#python AutoMailSender2.py 1