from .base import *
from .heroku import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    os.environ['LOCAL_IP'],
]
