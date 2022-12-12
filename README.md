# a simple backend for reformation
## Installation

```bash
cd backend
source env/bin/activate  # On Windows use env\Scripts\activate
py get-pip.py
pip install django
pip install djangorestframework
pip install django-rest-auth
```
[pip](https://pip.pypa.io/en/stable/)


## Run

```bash
cd backend
py manage.py makemigrations
py manage.py migrate
py manage.py runserver

http://127.0.0.1:8000/

py manage.py createsuperuser
admin
admin@admin.cl
admin123
```

