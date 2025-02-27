import smtplib # An email module that is necessary for this python project
from email.mime.multipart import MIMEMultipart # For creating emails with multiple parts
from email.mime.text import MIMEText # For plain text or html emails

# Defined function for sending emails 
def send_email(smtp_server, port, sender, password, recipients, subject, body)
# Variables for creating an email
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ','.join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
# For securing a connection with the SMTP server
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()
    
# SMTP Server and the 587 port that is commonly used for sending emails securely
smtp_server = 'smtp.gmail.com'
port = 587

email = "email@gmail.com" # Input the sender's email address
password = "password" # Input the password of the sender's email address

# Information to be entered by the user for sending emails
recipients = input("Recipients' Email Addresses (separated by comma): ").split(",")
subject = input("Subject: ")
body = input("Body: ")

print ("Your emails have been sent successfuly!✅")

# Calling the function
send_email(smtp_server, port, email, password, recipients, subject, body)
