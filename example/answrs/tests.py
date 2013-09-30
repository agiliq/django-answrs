"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from answrs.models import Question, Category, Answer


class AnswersAppTestcase(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username="admin", email="admin@agiliq.com", password="admin")
        self.category = Category(name='category_one', slug='category_one')
        self.category.save()
        self.question = Question(user=self.user, category=self.category, title='category Title', description='Nothing')
        self.question.save()
        self.ask_postdata = {u'category': [u'1'], u'description': [u'nothign'], u'title': [u'wow man']}
        self.cate_postdata = {u'name': [u'Job one']}
        self.answer = Answer(user=self.user, question=self.question, text='Nothing')
        self.answer.save()

    def test_Indexview(self):
        response = self.c.get(reverse("answrs_index"))
        self.assertEqual(200, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(reverse("answrs_index"))
        self.assertEqual(200, response.status_code)

    def test_randompageview(self):
        response = self.c.get(reverse("answrs_random"))
        self.assertEqual(302, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(reverse("answrs_random"))
        self.assertEqual(302, response.status_code)

    def test_askview(self):
        response = self.c.get(reverse("answrs_ask"))
        self.assertEqual(302, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(reverse("answrs_ask"))
        self.assertEqual(200, response.status_code)


    def test_askpost(self):
        response = self.c.post(reverse('answrs_ask'),self.ask_postdata)
        self.assertEqual(302, response.status_code)

    def test_askcatview(self):
        response = self.c.get(reverse("answrs_ask_cat", kwargs={'cat_slug':self.category.slug}))
        self.assertEqual(302, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(reverse("answrs_ask_cat", kwargs={'cat_slug':self.category.slug}))
        self.assertEqual(200, response.status_code)

    def test_anserview(self):
        response = self.c.get(reverse("answrs_answer", kwargs={'id':self.answer.id}))
        self.assertEqual(302, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(reverse("answrs_answer", kwargs={'id':self.answer.id}))
        self.assertEqual(200, response.status_code)

    def test_addcatview(self):
        response = self.c.get(reverse("answrs_add_cat"))
        self.assertEqual(302, response.status_code)
        self.c.login(username="admin", password="admin")
        response = self.c.get(reverse("answrs_add_cat"))
        self.assertEqual(200, response.status_code)

    def test_postcatview(self):
        response = self.c.post(reverse('answrs_add_cat'),self.cate_postdata)
        self.assertEqual(302, response.status_code)
