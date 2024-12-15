import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "karthikeya2006p@gmail.com"
sender_password = "Ravi"
recipient_email = "karthikeya2005p@gmail.com"

subject = "Automatic Email"
body = """\
Hello,

This is an automatically sent email using Python.

Best regards,
Your Automation
"""

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Send the email
try:
    with smtplib.SMTP("karthikeya2006p@gmail.com", 587) as server:  # Replace smtp.example.com with your email provider's SMTP server
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login to the email server
        server.sendmail(sender_email, recipient_email, message.as_string())  # Send the email
        print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
