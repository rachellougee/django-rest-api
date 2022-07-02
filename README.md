# django-rest-api

### Cloning the repository

Clone the repository

Move into the directory where we have the project files : 
```bash
cd django-rest-api

```

### Setup virtual environment :
Create a virtual environment to isolate our package dependencies locally
```bash
python3 -m venv env
source env/bin/activate 

```

### Install Django and Django REST framework into the virtual environment
```bash
pip install django
pip install djangorestframework

```

### Sync database for the first time
```bash
python manage.py migrate
# create local admin user
python manage.py createsuperuser --email xxxx@xxxxx.com --username xxxx

```

### Running the App

```bash
python manage.py runserver

```

the development server will be started at http://127.0.0.1:8000/


