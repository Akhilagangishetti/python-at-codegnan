import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()


SENDER_EMAIL = os.getenv('SENDER_EMAIL')     
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')       

def send_notification(receiver_email, visitor_name, purpose, visitor_id):
    try:
        subject = "New Visitor Arrived"
        body = (
            f"Hello,\n\n"
            f"A visitor has arrived to meet you.\n\n"
            f"Name: {visitor_name}\n"
            f"Purpose: {purpose}\n"
            f"Visitor ID: {visitor_id}\n\n"
            f"Please approve their pass at the reception.\n\n"
            f"Regards,\nVisitor Management System"
        )

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        server.quit()

        print(" Email notification sent successfully!")
    except Exception as e:
        print(f" Email not sent. Error: {e}")