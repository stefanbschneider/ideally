from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.utils import timezone
from django.template import loader
from django.forms import TextInput

from .models import Idea, Tag


class IndexView(generic.ListView):
    template_name = 'app/idea_index.html'
    context_object_name = 'idea_list'

    def get_queryset(self):
        """Return all ideas"""
        return Idea.objects.all().order_by('update_date')


# Idea views
class IdeaDetail(generic.DetailView):
    model = Idea
    template_name = 'app/idea_detail.html'


class IdeaCreate(CreateView):
    template_name = 'app/idea_form.html'
    model = Idea
    fields = ['title', 'description']


class IdeaUpdate(UpdateView):
    model = Idea
    fields = ['title', 'description']


class IdeaDelete(DeleteView):
    template_name = 'app/idea_delete.html'
    model = Idea
    success_url = reverse_lazy('app:index')


# Tag views
class TagIndex(generic.ListView):
    template_name = 'app/tag_index.html'
    context_object_name = 'tag_list'

    def get_queryset(self):
        return Tag.objects.all().order_by('name')


class TagDetail(generic.DetailView):
    model = Tag
    template_name = 'app/tag_detail.html'


class TagCreate(CreateView):
    template_name = 'app/tag_form.html'
    model = Tag
    fields = ['name', 'description', 'color']


class TagUpdate(UpdateView):
    model = Tag
    fields = ['name', 'description', 'color']

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields['name'].widget = TextInput(attrs={})
    #     return form


class TagDelete(DeleteView):
    template_name = 'app/tag_delete.html'
    model = Tag
    success_url = reverse_lazy('app:tag-index')
