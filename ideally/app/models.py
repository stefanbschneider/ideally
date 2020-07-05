from django.db import models
from django.urls import reverse


class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(default='', max_length=5000)
    creation_date = models.DateTimeField('date created', auto_now=True)
    update_date = models.DateTimeField('date updated', auto_now=True)
    # TODO: tags, photo, duration

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Absolute URL of an idea detail. Used for generic create/update views & model forms
        https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/#model-forms
        """
        return reverse('app:detail', kwargs={'pk': self.pk})
