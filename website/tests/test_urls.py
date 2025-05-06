from django.test import TestCase
from django.urls import reverse, resolve

from website.views import about_view, contact_view


class TestUrls(TestCase):
    def test_about_view_url(self):
        url = reverse("website:about_us")
        self.assertEqual(resolve(url).func, about_view)

    def test_contact_view_url(self):
        url = reverse("website:contact")
        self.assertEqual(resolve(url).func, contact_view)
