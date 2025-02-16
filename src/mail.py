import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject: str, content: str, recipient: str):
    smtp_server = os.getenv("MAIL_SERVER", "").strip()
    smtp_port = int(os.getenv("MAIL_PORT", 587))
    smtp_username = os.getenv("MAIL_USERNAME", "").strip()
    smtp_password = os.getenv("MAIL_PASSWORD", "").strip()
    sender_email = os.getenv("MAIL_FROM", "").strip()


    print(f"SMTP Server: '{smtp_server}'")
    print(f"SMTP Port: '{smtp_port}'")
    print(f"SMTP Username: '{smtp_username}'")


    if not smtp_server or not smtp_username or not smtp_password or not sender_email:
        print("❌ Error: One or more environment variables are missing!")
        return

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = subject
    message.attach(MIMEText(content, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient, message.as_string())
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {str(e)}")

if __name__ == "__main__":
    send_email(
        "Test Email from Ethereal",
        "This is a test email sent using Ethereal SMTP.",
        "test-recipient@example.com"
    )
