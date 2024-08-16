import smtplib
from email.message import EmailMessage

from celery import Celery
from config import SMTP_PASS,SMTP_USER

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks',broker='redis://localhost:6379')

def get_email_template_up_gymstatus(username: str, email_user,gym_status):
    email = EmailMessage()
    email['Subject'] = "EDWTHub Update Status!"
    email['From'] = SMTP_USER
    email['To'] = email_user

    email.set_content(
        '<div>'
        f'<h1 styles="color: green;"> Здравствуйте, {username}, вы достигли нового Gym Status</h1>'
        f'<h2 styles="color: green;">Новый статус {gym_status} </h2>'
        '</div>',
        subtype = 'html'
    )
    return email


def get_email_template_user_info(username,email_user, values: dict):
    email = EmailMessage()
    email['Subject'] = "EDWTHub Info Message"
    email['From'] = SMTP_USER
    email['To'] = email_user
    email.set_content(
        '<div>'
        f'<h1 styles="color: green;"> Здравствуйте, {username}, вот ваша статистика</h1>'
        f'<h3 styles="color: green;">Ваше имя {values["username"]}</h3>'
        f'<h3 styles="color: green;">email {values["email"]}</h3>'
        f'<h3 styles="color: green;">статус {values["gym_status"]}</h3>'
        f'<h3 styles="color: green;">Количество пройденных тренировок {values["count_workout"]}</h3>'
        f'<h3 styles="color: green;">вес {values["weight"]} кг</h3>'
        f'<h3 styles="color: green;">рост {values["height"]} см</h3>'
        f'<h3 styles="color: green;">направление {values["direction"]}</h3>'
        f'<h3 styles="color: green;">гендер {values["gender"]}</h3>'
        
        '</div>',
        subtype = 'html'
    )
    return email


def get_email_template_after_register(username,email_user):
    email = EmailMessage()
    email['Subject'] = "EDWTHub New Register User"
    email['From'] = SMTP_USER
    email['To'] = email_user
    email.set_content(
        '<div>'
        f'<h1 styles="color: green;"> Здравствуйте, {username}, вы успешно зарегестрировались на EDWeiss Training Hub</h1>'
        '</div>',
        subtype = 'html'
    )
    return email

def get_email_template_verification_user(email_user,code):
    email = EmailMessage()
    email['Subject'] = "EDWTHub Verification Code"
    email['From'] = SMTP_USER
    email['To'] = email_user
    email.set_content(
        '<div>'
        f'<h1 styles="color: green;"> Здравствуйте, ваш 6-значный код:</h1>'
        '<div>'
        f'<h1 styles="color: green;">{code}</h1>'
        '</div>'
        '</div>',
        subtype = 'html'
    )
    return email



#@celery.task
def send_email_up_gymstatus(username: str, email_user,gym_status):
    email = get_email_template_up_gymstatus(username,email_user,gym_status)
    with smtplib.SMTP_SSL(SMTP_HOST,SMTP_PORT) as server:
        server.login(SMTP_USER,SMTP_PASS)
        server.send_message(email)


def send_email_user_info(username: str, email_user,values):
    email = get_email_template_user_info(username,email_user,values)
    with smtplib.SMTP_SSL(SMTP_HOST,SMTP_PORT) as server:
        server.login(SMTP_USER,SMTP_PASS)
        server.send_message(email)


def send_email_after_registr(username: str,email_user):
    email = get_email_template_after_register(username,email_user)
    with smtplib.SMTP_SSL(SMTP_HOST,SMTP_PORT) as server:
        server.login(SMTP_USER,SMTP_PASS)
        server.send_message(email)

def send_verification_code(email,code):
    email = get_email_template_verification_user(email,code)
    with smtplib.SMTP_SSL(SMTP_HOST,SMTP_PORT) as server:
        server.login(SMTP_USER,SMTP_PASS)
        server.send_message(email)
    