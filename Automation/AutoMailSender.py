import os
import time
import psutil
import urllib3
import smtplib
import schedule

from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from urllib.request import urlopen

def is_connected():
  try:
     
    urllib3.urlopen("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox",timeout =1)
    return True
  except urllib3.URError as err:
    return False
  
def MailSender(filename,time):
  try:
    fromaddr = "ketanpython7@gmail.com"
    toaddr = "ketanhiraypatil@gmail.com"
    password = "blkphqgsbjmfqexf"
    #Password: blkp hqgs bjmf qexf
    
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr

    body = """
    Hello %s
    Welcome
    Please find attachment ducumnet which contains log of Running Process.

    Log file is created as : %s

    This is Auto generated mail.

    Thanks,
    Ketan
      """%(toaddr,time)
    
    Subject = """
            Marvellous Infosystems Process log gerated at: %s
       """%(time)
    
    msg['Subject'] = Subject

    msg.attach(MIMEText(body,'pain'))

    attachment = open(filename,"rb") #binary

    p = MIMEBase('application','octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Dispotion',"attachmnet; filename = %s" %filename)

    msg.attach(p)

    s= smtplib.SMTP('smtp.gmail.com',587)

    s.starttls()
    
    s.login(fromaddr,password)

    text =msg.as_string()

    s.sendmail(fromaddr,toaddr,text)

    s.quit()

    print("Log file successfully sent through Mail")

  except Exception as E:
     print("Unable to send mail",E)

def ProcessLog(log_dir ='Marvellous'):
  listprocess = []

  if not os.path.exists(log_dir):
    try:
      os.makedirs(log_dir)
    except:
      pass

  separator ="-"*80

  log_path = os.path.join(log_dir,"MarvellouLog%s.log"%(time.ctime()))

  f = open(log_path,'w')
  f.write(separator + "\n")
  f.write("Marvellous Infosystem Process Logger:" + time.ctime()+"\n")
  f.write(separator + "\n")
  f.write("\n")

  for proc in psutil.process_iter():
    try:
      pinfo= proc.as_dict(attrs=['pid','name','username'])
      vms = proc.memory_info().vms /(1024 * 1024)

      pinfo['vms']= vms
      listprocess.append(pinfo);
    except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
      pass
  
  for element in listprocess:
    f.write("%s\n" %element)

  print(" Log file is successfully generated at location %s",(log_path))

  connected = is_connected()

  if connected:
    starTime = time.time()
    MailSender(log_path,time.ctime())
    endTime = time.time()

    print('Took %s seconds to send mail' %(endTime -starTime))
 
  else:
   print("There is no internat conncection")



def main():

  print("---- Marvellous Infosytem by piyush kahirnar----")

  print("Application name:"+argv[0])

  if(len(argv)!=2 ):
    print("Error:Invalid number of argument")
    exit()
  
  if(argv[1] == "-h" or argv[1] == "-H"):
     print("This automation script is used log recording of running processess")
     exit()
  
  if(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
    
        print("usage:Application AbsolutePath_of_directory")
        exit()

  try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
          schedule.run_pending()
          time.sleep(1)
    
  except ValueError:
        print("Error: Invalid datatype of input")

  except Exception as E:
     print("Error: Invalid input",E)


if __name__ =="__main__":
   main()

