import sys
import os

from django.conf import settings
from tests import test_settings

#add the dir one level up to PYTHONPATH so we can import stuff for testing
sys.path.append('../')
sys.path.append('./tests')


try:
    settings.configure(test_settings, DEBUG=True)
except:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    from django.test.utils import setup_test_environment
    setup_test_environment()
