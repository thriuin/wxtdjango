# wxtdjango 

Simple demo of using Django to server WET-BOEW compliant website.
Tested with Python 3.

## Installation:

  1. Create a virtual environment for the project and install the 
     requirements from the requirementst.txt file
  2. Download WET templates to the root directory from:
      https://github.com/wet-boew/GCWeb/releases/download/v4.0.27/themes-dist-4.0.27-gcweb.zip
  3. Rename the db.sqlite3.sample file to db.sqllite3 

## Commonly used Django commands

```commandline
python manage.py runserver
django-admin startapp wxtdemo
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

