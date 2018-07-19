# Please configure a real secret key in instance/config.py
import os

# Root path
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY')

TESTING = False

# Connection string
SQLALCHEMY_DATABASE_URI = os.environ.get('OPENSCHUFA_DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO_POOL = True

UPLOADED_PHOTOS_DEST = APP_ROOT + '/media/'

MAIL_DEFAULT_SENDER = 'id@openschufa.de'
MAIL_USE_TLS = True
MAIL_SERVER = 'in-v3.mailjet.com'
MAIL_PORT = 587
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


