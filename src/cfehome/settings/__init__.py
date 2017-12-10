# currently working in 
# /home/martynov/Downloads/django1.11/cfehome/src/cfehome/settings
from .base import *

from .production import *

try:
   from .local import *
except:
   pass
