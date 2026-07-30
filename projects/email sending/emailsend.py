

#import required modules
import smtplibfrom 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# server config parameters
SMTP_SERVER = "smtp.gmail.com"
SMPT_PORT = 587
SENDER_EMAIL = "Your email"
PASSKEY = "YOU app passkey"


def singleEmailSend(to_email:str, subject:str, body:str):
    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['From'] = SENDER_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        # start server
        server = smtpliB.SMTP(SMTP_SERVER, SMPT_PORT)
        # start server
        server.starttls()
        #login to server
        server.login(SENDER_EMAIL, PASSKEY)
        # send email
        server.sendmail(SENDER_EMAIL, to_email,msg.as_string())
        # quit server
        server.quit()
        return "Successfully email send"
    except Exception as e:
        return f"something wrong while sending an email to {to_email}:{e}"

# read inputs
email = input("Enter Receiver email address:")
subject = input("Enter enail subject:")
body = input("Enter email body:")
print(singleEmailSend(to_email))


