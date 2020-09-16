from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from colorfield.fields import ColorField


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    color = models.CharField(max_length=7, default='#FF0000')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:tag-detail', kwargs={'pk': self.pk})


class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    creation_date = models.DateTimeField('date created', auto_now=True)
    update_date = models.DateTimeField('date updated', auto_now=True)
    # cascade: delete idea when owner is deleted
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # access tags via <idea>.tags.all(); or vice versa: <tag>.idea_set.all()
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    # image = models.ImageField(default='app/icons8-idea-512.png')
    # TODO: photo, duration

    @property
    def user_tags(self):
        """All tags that belong to the owner"""
        return Tag.objects.filter(owner=self.owner).order_by('name')

    def has_tag(self, tag):
        return Tag.objects.filter(id=tag.id, )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Absolute URL of an idea detail. Used for generic create/update views & model forms
        https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/#model-forms
        """
        return reverse('app:detail', kwargs={'pk': self.pk})
