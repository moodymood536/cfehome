#cfehome<br>
<b>Trying django 1.11.8 </b><br>
Creating new blank project. The tutorial link https://www.codingforentrepreneurs.com/blog/create-a-blank-django-project/ <br>
<b>#To create blank django project(For Linux Ubuntu) we need to create virtual environment and working folders</b><br>
mkdir cfehome && cd cfehome<br>
virtualenv -p python3 . <br>
<b>#Do not forget To activate virtualenv. Virtualenv helps you to leave PC clean evenwith 100500 projects on it.</b> <br>
source bin/activate<br>
<b>#install django and start project</b><br>
pip install django==1.11.8<br>
mkdir src && cd src<br>
django-admin.py startproject cfehome .<br>
<b>#creating new settings module - it is not requirement, just good move</b><br>
cd cfehome<br>
mkdir settings && cd settings<br>
<b>#creating __init__.py NOT SHURE WHY FOR NOW (need to discover). Tutorial says - to make it a module</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;echo "from .base import *<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;from .production import *<br>
&nbsp;&nbsp;&nbsp;&nbsp;try:<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;from .local import *<br>
&nbsp;&nbsp;&nbsp;&nbsp;except:<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pass<br>
&nbsp;&nbsp;&nbsp;&nbsp;" > __init__.py<br>
<b>#change BASE_DIR in settins.py (changing default path to files)</b><br>
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))<br>
<b>#to</b> <br>
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),br>
<b>#move default settings.py into new settings module and rename settings.py to base.py</b><br>
mv ~/Dev/cfehome/src/cfehome/settings.py ~/Dev/cfehome/src/cfehome/settings/base.py<br>
<b>#copy local settings to make new (base.py and production.py)<br>
cp ~/Dev/cfehome/src/cfehome/settings/base.py ~/Dev/cfehome/src/cfehome/settings/local.py</b><br>

cp ~/Dev/cfehome/src/cfehome/settings/base.py ~/Dev/cfehome/src/cfehome/settings/production.py<br>
<b>#create requirements.txt</b><br>
pip freeze > requirements.txt <br>
<b>#run migration and create superuser</b><br>
python manage.py migrate<br>
pythom manage.py create suoeruser<br>
