![Django CI](https://github.com/stefanbschneider/ideally/workflows/Django%20CI/badge.svg)

# Ideally: Organize & Grow Your Ideas

* ideally.ml
* https://ideally-app.herokuapp.com/

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
* `DATABASE_URL`: URL to Heroku Postgres DB
* `SENDGRID_API_KEY`: `<sendgrid-api-key>`

## Todos

* Favicon
* PWA: https://github.com/silviolleite/django-pwa
* search, sort, filter ideas based on tags and create/update time
* fix image upload
* add milestones, notes to ideas
* improve usability by asking others what to improve

