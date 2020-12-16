from django.forms import ModelForm

from . import models


class IdeaForm(ModelForm):
    class Meta:
        model = models.Idea
        fields = ['title', 'description', 'tags']


class NoteForm(ModelForm):
    class Meta:
        model = models.Note
        fields = ['title', 'note']
