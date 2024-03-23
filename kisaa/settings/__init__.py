import os
from .base import *


if os.environ.get('DJANGO_ENV', None) == 'prod':
    from .prod import *
    print("Production settings loaded from prod.py file")
elif os.environ.get('DJANGO_ENV', None) == 'test':
    from .test import *
    print("test settings loaded from test.py file")
elif os.environ.get('DJANGO_ENV', None) == 'dev':
    from .dev import *
    print("development settings loaded from dev.py file")
else:
    print("Environment value Not set/invalid!")
    from .local import *
    print("local settings loaded from local.py file")

# try:
#     if os.environ['DJANGO_ENV'] == 'prod':
#         from .prod import *
#         print("Production settings loaded from prod.py file")
#     elif os.environ['DJANGO_ENV'] == 'test':
#         from .test import *
#         print("test settings loaded from test.py file")
#     elif os.environ['DJANGO_ENV'] == 'dev':
#         from .dev import *
#         print("development settings loaded from dev.py file")
#     else:
#         print("Environment value Not set/invalid!")
# except Exception as e:
#     print(f"exception {e} occured while initiating settings in __init__.py file.")
#     from .local import *
#     print("local settings loaded from local.py file")
