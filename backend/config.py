from dotenv import load_dotenv
import os


load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_PORT")
SECRET_AUTH = os.environ.get("SECRET_AUTH")
SECRET_USER_MANAGER = os.environ.get("SECRET_USER_MANAGER")
SMTP_PASS= os.environ.get("SMTP_PASS")
