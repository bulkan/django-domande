#import sys
#import os

##add the dir one level up to PYTHONPATH so we can import stuff for testing
#sys.path.append('../')
#sys.path.append('./tests')

#from tests import test_settings


#try:
#settings.configure(test_settings, DEBUG=True)
    #except:
    #os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    #from django.test.utils import setup_test_environment
#setup_test_environment()


    #from django.core.management import call_command

    #call_command('syncdb', interactive=False)
    #call_command('migrate', interactive=False)
