![Django CI](https://github.com/stefanbschneider/ideally/workflows/Django%20CI/badge.svg)

# Ideally: Organize & Grow Your Ideas

## Usage



## Deployment

### Local

```
# serve
python manage.py runserver

# test
python manage.py test app
```

### Heroku

Deployment is automatically updated with new pushes to `master`.

Set the following config vars in Heroku (= env vars):

* `DJANGO_SETTINGS_MODULE`: `project.prod_settings`
* `DJANGO_SECRET_KEY`: `<randomly-generated-secret-key>`

## Todos

* Color picking, saving, adding tags
* add/remove tags
* CI/CD with tests & deployment on heroku
* Afterwards: Authentication & users
* Make a reusable tag component that displays the tag as badge in the right color + description on mouse over + clickable to get to tag detail
    * Without having to define it anew in each html template (eg, idea detail, tag index, tag detail)
