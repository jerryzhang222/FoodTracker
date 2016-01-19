import django


import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'bankfood_proj.settings'
django.setup()
#print(os.environ['DJANGO_SETTINGS_MODULE'])
#os.environ['PYTHONPATH']= "/home/jerryzhang/bankfood"
#try:
#    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
#except KeyError:
#    user_paths = []
    
#print user_paths