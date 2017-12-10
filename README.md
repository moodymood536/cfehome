# cfehome
Trying django 1.11.8 
1. Creating new blank project. The tutorial link https://www.codingforentrepreneurs.com/blog/create-a-blank-django-project/ <br>
#To create blank django project(For Linux Ubuntu) we need to create virtual environment and working folders<br>
mkdir cfehome && cd cfehome<br>
virtualenv -p python3 . <br>
#Do not forget To activate virtualenv. Virtualenv helps you to leave PC clean evenwith 100500 projects on it. <br>
source bin/activate<br>
#install django and start project<br>
pip install django==1.11.8<br>
mkdir src && cd src<br>
django-admin.py startproject cfehome .<br>
#creating new settings module - it is not requirement, just good move<br>
cd cfehome<br>
mkdir settings && cd settings<br>
#creating __init__.py NOT SHURE WHY FOR NOW (need to discover). Tutorial says - to make it a module<br>
echo "from .base import *<br>

from .production import *<br>

try:<br>
   from .local import *<br>
except:<br>
   pass<br>
" > __init__.py<br>
#change BASE_DIR in settins.py (changing default path to files)<br>
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))<br>
# to<br>
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),br>
#move default settings.py into new settings module and rename settings.py to base.py<br>
mv ~/Dev/cfehome/src/cfehome/settings.py ~/Dev/cfehome/src/cfehome/settings/base.py<br>
#copy local settings to make new (base.py and production.py)<br>
cp ~/Dev/cfehome/src/cfehome/settings/base.py ~/Dev/cfehome/src/cfehome/settings/local.py<br>

cp ~/Dev/cfehome/src/cfehome/settings/base.py ~/Dev/cfehome/src/cfehome/settings/production.py
#create requirements.txt
pip freeze > requirements.txt
#run migration and create superuser
python manage.py migrate
pythom manage.py create suoeruser
