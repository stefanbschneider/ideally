![Django CI](https://github.com/stefanbschneider/ideally/workflows/Django%20CI/badge.svg)

# Ideally: Organize & Grow Your Ideas

```
# serve
python manage.py runserver

# test
python manage.py test app
```

## Todos

* Color picking, saving, adding tags
* add/remove tags
* CI/CD with tests & deployment on heroku
* Afterwards: Authentication & users
* Make a reusable tag component that displays the tag as badge in the right color + description on mouse over + clickable to get to tag detail
    * Without having to define it anew in each html template (eg, idea detail, tag index, tag detail)
