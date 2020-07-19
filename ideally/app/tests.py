import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Idea, Tag


def create_idea(title, description):
    return Idea.objects.create(title=title, description=description)


def create_tag(name, description):
    return Tag.objects.create(name=name, description=description)


class IdeaIndexTests(TestCase):
    def test_no_ideas(self):
        """If no idea exists, an appropriate message is displayed."""
        response = self.client.get(reverse('app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No ideas added yet.")
        self.assertQuerysetEqual(response.context['idea_list'], [])
