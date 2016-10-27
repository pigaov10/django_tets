# -*- coding: utf-8 -*-
import pytest
# from mixer.backend.django import mixer
# from django.test import TestCase

@pytest.mark.django_db
class TestCustomer:
    def test_model(self, client):
        obj = client.get('/polls/customer/detail')
        assert obj.status_code == 404, 'Cria instancia customer'


# -*- coding: utf-8 -*-
# import pytest
# from mixer.backend.django import Mixer
# from django.test import TestCase
# from meuprojeto.polls.models import Customer, Category
# from datetime import datetime
#
# class TestCustomer(TestCase):
#     def setUp(self):
#         # obj = Category.objects.get(name='Bebidas')
#         Category.objects.create(name="Moveis")
#
#     def test_category_instance_created_object(self):
#         objeto = Category.objects.get(name="Moveis")
#         self.assertEqual(objeto.name, 'Moveis')
