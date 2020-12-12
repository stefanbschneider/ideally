from django.forms import ModelForm

from .models import Idea


class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'tags']
