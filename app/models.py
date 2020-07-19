from django.db import models
from django.urls import reverse
from colorfield.fields import ColorField


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    color = ColorField(default='#FF0000')
    # ideas = models.ManyToManyField(Idea)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:tag-detail', kwargs={'pk': self.pk})


class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    creation_date = models.DateTimeField('date created', auto_now=True)
    update_date = models.DateTimeField('date updated', auto_now=True)
    # access tags via <idea>.tags.all(); or vice versa: <tag>.idea_set.all()
    tags = models.ManyToManyField(Tag)
    # TODO: photo, duration

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Absolute URL of an idea detail. Used for generic create/update views & model forms
        https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/#model-forms
        """
        return reverse('app:detail', kwargs={'pk': self.pk})
