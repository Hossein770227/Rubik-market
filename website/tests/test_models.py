from django.test import TestCase
from model_bakery import baker
from website.models import Contact


class TestContactModel(TestCase):
    def test_model_str(self):
        Contact=baker.make('Contact', email='hossein.h.a770227@gmail.com', message_subject='subject text')
        self.assertEqual(str(Contact),'hossein.h.a770227@gmail.com:subject text' )
