# cfehome
Trying django 1.11.8 
1. Creatin new blank project. The tutorial link https://www.codingforentrepreneurs.com/blog/create-a-blank-django-project/
#To create blank django project(For Linux Ubuntu) we need to create virtual environment and working folders
mkdir cfehome && cd cfehome
virtualenv -p python3 . 
#Do not forget To activate virtualenv. Virtualenv helps you to leave PC clean evenwith 100500 projects on it. 
source bin/activate
#install django and start project
pip install django==1.11.8
mkdir src && cd src
django-admin.py startproject cfehome .
#creating new settings module - it is not requirement, just good move
cd cfehome
mkdir settings && cd settings
#creating __init__.py NOT SHURE WHY FOR NOW (need to discover). Tutorial says - to make it a module
echo "from .base import *

from .production import *

try:
   from .local import *
except:
   pass
" > __init__.py
#change BASE_DIR in settins.py (changing default path to files)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# to
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#move default settings.py into new settings module and rename settings.py to base.py
mv ~/Dev/cfehome/src/cfehome/settings.py ~/Dev/cfehome/src/cfehome/settings/base.py
#copy local settings to make new (base.py and production.py)
cp ~/Dev/cfehome/src/cfehome/settings/base.py ~/Dev/cfehome/src/cfehome/settings/local.py

cp ~/Dev/cfehome/src/cfehome/settings/base.py ~/Dev/cfehome/src/cfehome/settings/production.py
#create requirements.txt
pip freeze > requirements.txt
#run migration and create superuser
python manage.py migrate
pythom manage.py create suoeruser
