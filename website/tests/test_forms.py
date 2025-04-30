from django.test import TestCase

from accounts.models import MyUser
from website.forms import ContactForm

class ContactFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user =MyUser.objects.create_user(phone_number='09211234567', full_name='hossein hadi amani', password='password' )

    def test_validate_data(self):
        form = ContactForm(data={'user':self.user, 'email':'hossein.h.a770227@gamil.com', 'message_subject':'subject text' , 'message':'sample message'})
        self.assertTrue(form.is_valid())
    
    def test_empty_data(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)