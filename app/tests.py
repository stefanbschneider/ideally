from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from freezegun import freeze_time

from .models import Idea, Tag


class IdeaIndexTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user('temporary', 'temp@gmail.com', 'temporary')
        self.client.login(username='temporary', password='temporary')

    def create_idea(self, title, description):
        # setting creation or update date manually doesn't work since they are auto-set to now
        return Idea.objects.create(title=title, description=description, owner=self.user)

    def test_no_ideas(self):
        """If no idea exists, an appropriate message is displayed."""
        response = self.client.get(reverse('app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No ideas added yet.")
        self.assertQuerysetEqual(response.context['idea_list'], [])

    def test_one_two_ideas(self):
        """Create two ideas and test if they are listed (newest first)"""
        # use freezegun to test time-dependent behavior: create first idea1, then 2
        # without that, ordering get sometimes messed up
        with freeze_time('2020-01-01') as frozen_datetime:
            self.create_idea('idea one', 'description1')
            response = self.client.get(reverse('app:index'))
            self.assertQuerysetEqual(response.context['idea_list'], ['<Idea: idea one>'])

            frozen_datetime.move_to('2020-01-02')
            self.create_idea('idea two', 'descr2')
            response = self.client.get(reverse('app:index'))
            self.assertQuerysetEqual(response.context['idea_list'], ['<Idea: idea two>', '<Idea: idea one>'])


class TagIndexTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user('temporary', 'temp@gmail.com', 'temporary')
        self.client.login(username='temporary', password='temporary')

    def create_tag(self, name, description):
        return Tag.objects.create(name=name, description=description, owner=self.user)

    def test_no_tags(self):
        """If no tag exists, an appropriate message is displayed."""
        response = self.client.get(reverse('app:tag-index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tags added yet.")
        self.assertQuerysetEqual(response.context['tag_list'], [])

    def test_one_two_tags(self):
        """Create two tags and test if they are listed (alphabetical order)"""
        self.create_tag('B tag', 'description1')
        response = self.client.get(reverse('app:tag-index'))
        self.assertQuerysetEqual(response.context['tag_list'], ['<Tag: B tag>'])

        # move forward in time
        self.create_tag('A tag', 'descr2')
        response = self.client.get(reverse('app:tag-index'))
        self.assertQuerysetEqual(response.context['tag_list'], ['<Tag: A tag>', '<Tag: B tag>'])
