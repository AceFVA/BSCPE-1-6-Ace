import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(smtp_server, port, sender, password, recipients, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ','.join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()
    
smtp_server = 'smtp.gmail.com'
port = 587

email = "acefrancisagustin@gmail.com"
password = "yfumaomnxgduecge"

recipients = input("Recipients' Email Addresses (separated by comma): ").split(",")
subject = input("Subject: ")
body = input("Body: ")

print ("Your emails have been sent successfuly!✅")

send_email(smtp_server, port, email, password, recipients, subject, body)
