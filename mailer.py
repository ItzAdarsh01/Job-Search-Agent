import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_job_email(job_analysis):
    sender_email = "kas0adarsh404@gmail.com"
    
    # 1. Define your array (list) of receivers
    receiver_emails = [
        "adarsh171101@gmail.com",
    ]
    
    app_password = "hldoioymakidsqex"

    # Email Header
    message = MIMEMultipart()
    message["From"] = sender_email
    
    # 2. Join the list into a single string for the 'To' header
    message["To"] = ", ".join(receiver_emails)
    message["Subject"] = "JOB AUTOMATION - Today's Top Job Matches for You :)"

    # Email body
    body = f"Hello Bro,\n\nHere are your job matches for today:\n\n{job_analysis}\n\nGood luck!"
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            
            # 3. Pass the actual list to sendmail
            server.sendmail(sender_email, receiver_emails, message.as_string())
            
        print(f"\n Email successfully sent to: {', '.join(receiver_emails)}")
    except Exception as e:
        print(f"\n Email Error: {e}")