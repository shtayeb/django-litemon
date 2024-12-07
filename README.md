# django-litemon (WIP)
django-litemon is a lighweight monitoring app for Django.

Detailed documentation is in the "docs" directory.

## Plan


## Quick start

1. Add "django_litemon" to your INSTALLED_APPS setting like this::

```python
    INSTALLED_APPS = [
        ...,
        "django_litemon",
    ]
```

2. Include the polls URLconf in your project urls.py like this::

```python
    path("litemon/", include("django_litemon.urls")),
```

3. Run ``python manage.py migrate`` to create the models.

4. Start the development server and visit the admin to create a poll.

5. Visit the ``/litemon`` URL.

## Development
Clone repo
```shell
git clone https://github.com/shtayeb/django-litemon.git
```

Test App
```python
cd tests

python manage.py runserver
```


