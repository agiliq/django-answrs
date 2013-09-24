"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse



class AnswersAppTestcase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_Indexview(self):
        response = self.c.get(reverse("answrs_index"))
        self.assertEqual(200, response.status_code)
