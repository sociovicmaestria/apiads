# API Python Django - Grupo 03 - Ambientes de Desarrollo de Software

## Packages included:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](http://www.django-rest-framework.org/)
- [Coreapi](https://pypi.org/project/django-coreapi/)
- [Django Filter](https://django-filter.readthedocs.io/en/master/)
- [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html)

## Description

This is an API project on Python - Django for the ADS final project

## Installation

### Pre Requisites

#### Install Python

Download Python installer for the [official Page](https://www.python.org/downloads/)

#### Install Pip

```
python -m pip install -U pip
```

#### Install Virtualenv

```
pip install virtualenv
virtualenv env
env\Script\activate
```

#### Install Main Packages

```
pip install Django
pip install djangorestframework
pip install coreapi
pip install django-filter
pip install djoser
pip install djangorestframework_simplejwt
```

#### Configure Mysql Connection

```
pip install mysqlclient
```

- If you have any errors, check your python version and download the correct [mysqlclient](https://www.lfd.uci.edu/~gohlke/pythonlibs/?source=post_page-----f946d0f6f9e3----------------------) and try with:

```
pip install mysqlclient-1.3.13-cp37-cp37m-win32.whl
```

- Don't forget put the connection parameters in DATABASES section in the settings.py file

### Clone Repository

```
git clone ...
cd apiads
```

## Getting Started

### Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### Create Super User

```
python manage.py createsuperuser
```

### Load Initial Data

```
python manage.py loaddata initial_data
```

### Development

```
python manage.py runserver
```

## Production Mode

- Generate the static files

```
python manage.py collectstatic
```

- Consider the files below to deploy the app in Pivotal Cloud Foundry

    manifest.yml
    runtime.txt
    requirements.txt
    Procfile    

- Run task with Pivotal. E.g.

```
cf run-task django-api "python manage.py migrate" --name migrate
```

Brought to you by [Grupo 03](https://acme.com)
