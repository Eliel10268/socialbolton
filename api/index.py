import sys 
import os

sys.path.append(os.path.dirname (os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social.settings")

from django.core.wsgi import get_wsgi_application 

from magnum import Magnum



application = get_wsgi_application()

handler = Magnum(application)