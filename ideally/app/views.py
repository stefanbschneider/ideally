from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.utils import timezone
from django.template import loader

from .models import Idea


class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'idea_list'

    def get_queryset(self):
        """Return all ideas"""
        return Idea.objects.all().order_by('update_date')
