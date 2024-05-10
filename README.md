# Music_playlist_django


## Documentation

[Music_api](https://linktodocumentation)

## Setup a Virtual Environment (optional but recommended) [pip](https://pip.pypa.io/en/stable/) 
```
Install virtualenv if you don't have it: pip install virtualenv
Create a new virtual environment: virtualenv env
```
## Activate the virtual environment:
`` 
On Windows: env\Scripts\activate
On Unix/Linux: source env/bin/activate 
``



## Install Django and Django REST Framework
```
Install Django: pip install django
Install Django REST Framework: pip install djangorestframework
```

## Create a new Django project
```
Run: django-admin startproject myproject
This will create a new folder myproject with some initial files.
```

## Create a new Django app
```
Navigate into the project folder: cd myproject
Run: python manage.py startapp music_api
This will create a new folder music_api within the project.
```

## Add the app to INSTALLED_APPS
```
Open myproject/settings.py file.
Find the INSTALLED_APPS list and add 'music_api' and 'rest_framework' to it.
```
## Create the database migrations
```
Run: python manage.py makemigrations music_api
Run: python manage.py migrate
```

## Add the URL pattern
```
# Open myproject/urls.py file.
# Import the include function: from django.urls import include
# Add the following line to urlpatterns: path('', include('music_api.urls')),
```


## Run the development server

``` 
Run: python manage.py runserver
# You should see the server start at {' http://127.0.0.1:8000/' }
```


## Test the API endpoints
`
You can now test the API endpoints using tools like Postman or cURL.
For example, to create a new song, send a POST request to http://127.0.0.1:8000/music-api/songs/ with a JSON payload like {"name": "La Vie en Rose", "artist": "Edith Piaf", "release_year":
