DEBUG = False
BROKER = 'redis://redis:6379/0'

MONGO_DB = 'tipi'
MONGO_HOST = 'db'
MONGO_PORT = 27017
MONGO_USER = ''
MONGO_PASSWORD = ''

VALIDATION_EMAIL_SUBJECT = 'Validación de Alerta'
SPARKPOST_API = 'XXXXXXXXXXXXXXXXXXXXXXX'
FROM_EMAIL = 'test@example.com'

TEMPLATE_DIR = None

try:
    from local_config import *
except:
    pass
