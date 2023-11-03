import os
import hashlib
import shutil
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Function to calculate the checksum of a file
def calculate_checksum(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Function to find duplicate files in a directory
def find_duplicate_files(directory):
    file_checksums = {}
    duplicate_files = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            checksum = calculate_checksum(file_path)
            if checksum in file_checksums:
                duplicate_files.append((file_path, file_checksums[checksum]))
            else:
                file_checksums[checksum] = file_path

    return duplicate_files

# Function to delete duplicate files and create a log
def delete_duplicate_files_and_log(directory):
    duplicates = find_duplicate_files(directory)

    if not duplicates:
        return

    log_file_name = "Marvellous/DuplicateRemovalLog_{}.txt".format(time.strftime("%Y%m%d-%H%M%S"))
    os.makedirs(os.path.dirname(log_file_name), exist_ok=True)

    with open(log_file_name, "w") as log_file:
        for duplicate in duplicates:
            duplicate_path, original_path = duplicate
            log_file.write("Deleted duplicate file: {}\n".format(duplicate_path))
            os.remove(duplicate_path)

    return log_file_name, len(duplicates)

# Function to send an email with statistics
def send_email(sender_email, receiver_email, log_file, start_time, total_duplicates):
    subject = "Duplicate File Removal Report"
    message = MIMEMultipart()

    password = "blkphqgsbjmfqexf"
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText("Starting time of scanning: {}\n".format(start_time)))
    message.attach(MIMEText("Total number of duplicate files found: {}\n".format(total_duplicates)))

    with open(log_file, "rb") as attachment:
        part = MIMEApplication(attachment.read())
        part.add_header("Content-Disposition", "attachment; filename=DuplicateRemovalLog.txt")
        message.attach(part)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email: ", str(e))

# Command line options and script execution
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Duplicate File Removal Script")
    parser.add_argument("directory", help="Absolute path of the directory with duplicate files")
    parser.add_argument("interval", type=int, help="Time interval for script execution (in minutes)")
    parser.add_argument("receiver_email", help="Email ID of the receiver")

    args = parser.parse_args()

    while True:
        start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        result = delete_duplicate_files_and_log(args.directory)
        if result:
            log_file, total_duplicates = result
            send_email("ketanpython7@gmail.com", args.receiver_email, log_file, start_time, total_duplicates)
        else:
            print("No duplicate files found.")
        time.sleep(args.interval * 60)  # Convert minutes to seconds
