from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Idea, Tag


def create_idea(title, description):
    # setting creation or update date manually doesn't work since they are auto-set to now
    return Idea.objects.create(title=title, description=description)


def create_tag(name, description):
    return Tag.objects.create(name=name, description=description)


class IdeaIndexTests(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temp@gmail.com', 'temporary')
        # TODO: also test that pages are not accessible without login!
        # FIXME: fix tests

    def test_no_ideas(self):
        """If no idea exists, an appropriate message is displayed."""
        # login first to access idea list: https://stackoverflow.com/a/7367945/2745116
        User = get_user_model()
        self.client.login(username='temporary', password='temporary')

        response = self.client.get(reverse('app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No ideas added yet.")
        self.assertQuerysetEqual(response.context['idea_list'], [])

    def test_one_two_ideas(self):
        """Create two ideas and test if they are listed (newest first)"""
        # login first to access idea list: https://stackoverflow.com/a/7367945/2745116
        User = get_user_model()
        self.client.login(username='temporary', password='temporary')

        create_idea('idea one', 'description1')
        response = self.client.get(reverse('app:index'))
        self.assertQuerysetEqual(response.context['idea_list'], ['<Idea: idea one>'])

        create_idea('idea two', 'descr2')
        response = self.client.get(reverse('app:index'))
        self.assertQuerysetEqual(response.context['idea_list'], ['<Idea: idea two>', '<Idea: idea one>'])


class TagIndexTests(TestCase):
    def test_no_tags(self):
        """If no tag exists, an appropriate message is displayed."""
        response = self.client.get(reverse('app:tag-index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tags added yet.")
        self.assertQuerysetEqual(response.context['tag_list'], [])

    def test_one_two_tags(self):
        """Create two tags and test if they are listed (alphabetical order)"""
        create_tag('B tag', 'description1')
        response = self.client.get(reverse('app:tag-index'))
        self.assertQuerysetEqual(response.context['tag_list'], ['<Tag: B tag>'])

        create_tag('A tag', 'descr2')
        response = self.client.get(reverse('app:tag-index'))
        self.assertQuerysetEqual(response.context['tag_list'], ['<Tag: A tag>', '<Tag: B tag>'])
