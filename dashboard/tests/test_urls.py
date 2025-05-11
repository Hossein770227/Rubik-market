
from django.test import TestCase
from django.urls import reverse, resolve

from accounts.models import MyUser
from dashboard.models import Address
from dashboard.views import AddressView, DeleteAddressView, UpdateAddressView, personal_info

class TestUrls(TestCase):
    def setUp(self):
        self.user =MyUser.objects.create_user(phone_number='09211234567', full_name='hossein hadi amani', password='password' )
        self.address = Address.objects.create(user=self.user, province='Hamadan', city='asadabad', full_address = 'example address', postal_code = '12345678910')
        self.id = self.address.pk

    def test_personal_info_url(self):
        url = reverse('dashboard:personal_info')
        self.assertEqual(resolve(url).func, personal_info)

    def test_address_view_class_url(self):
        url = reverse('dashboard:address')
        self.assertEqual(resolve(url).func.view_class, AddressView)

    def test_update_address_view_class(self):
        url = reverse('dashboard:update_address', args=[self.id])
        self.assertEqual(resolve(url).func.view_class, UpdateAddressView)
    
    def test_delete_address_view_class(self):
        url = reverse('dashboard:delete_address', args=[self.id])
        self.assertEqual(resolve(url).func.view_class, DeleteAddressView)