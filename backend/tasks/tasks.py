import smtplib
from email.message import EmailMessage

from celery import Celery
from config import SMTP_PASS

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

#celery = Celery('tasks',broker='')