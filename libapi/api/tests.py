from django.contrib.auth.models import User
from django.test import TestCase
from .models import Author


class AuthorTest(TestCase):

    def setUp(self):
        User.objects.create_user(
            'TestUser',
            email=None,
            password=None
        )

        Author.objects.create(
            name='Leonardo Tosin'
        )

    def test_user(self):
        base_user = User.objects.get(username='TestUser')
        self.assertNotEqual(base_user.id, 0)

    def test_find_author(self):
        author = Author.objects.get(name='Leonardo Tosin')
        self.assertNotEqual(author.id, 0)
