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
