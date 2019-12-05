API Python Django - Grupo 03 - Ambientes de Desarrollo de Software
======================================================

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
```

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

### Load Initial Data
```
python manage.py loaddata initial_data
```

### Create Super User
```
python manage.py createsuperuser

```

### Development
```
python manage.py runserver

```

Brought to you by [Grupo 03](https://acme.com)
