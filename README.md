# drf_project

Django Rest Framework tutorials

### Django REST Framework series - Setup and Models

### Create command for populate data db

```
 management/
        __init__.py
        commands/
            __init__.py
            _private.py
            populate_db.py
```

### Run the command

```
python manage.py populate_db
```

### Install django-silk package

- For analysis query and request

```
pip install django-silk

MIDDLEWARE = [
    ...
    'silk.middleware.SilkyMiddleware',
    ...
]

INSTALLED_APPS = (
    ...
    'silk'
)

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

python manage.py migrate

python manage.py collectstatic
```
