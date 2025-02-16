from celery import Celery
from src.mail import send_email

c_app = Celery()
c_app.config_from_object("src.config")

@c_app.task()
def send_email_task(recipients: list[str], subject: str, body: str):
    for recipient in recipients:
        send_email(subject=subject, content=body, recipient=recipient)
    print("Emails sent")
