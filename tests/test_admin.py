#!/usr/bin/env python

"""
test_django-admin-user-summary
------------

Tests for `django-admin-user-summary` models module.
"""

from collections import OrderedDict

from django.contrib.auth import get_user_model
from django.test import TestCase, Client

django_user_model = get_user_model()


class TestDjangoAdminUserSummary(TestCase):

    def setUp(self):
        user_data = OrderedDict(
            mypassword='admin',
            email='adminemail@test.com',
            password='adminpassword'
        )
        self.user = django_user_model.objects.create_superuser(
            *user_data.values())

        self.client = Client()

        login_data = user_data
        del login_data['email']

        self.client.login(**user_data)

    def test_something(self):
        self.client.get('/admin/stats/usersummary/')

    def tearDown(self):
        self.user.delete()
