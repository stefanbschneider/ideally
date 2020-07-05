from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.utils import timezone
from django.template import loader

from .models import Idea, Tag


class IndexView(generic.ListView):
    template_name = 'app/index.html'
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
class TagDetail(generic.DetailView):
    model = Tag
    template_name = 'app/tag_detail.html'
