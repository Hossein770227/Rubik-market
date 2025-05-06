from django.test import TestCase , Client
from django.urls import reverse

class AboutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_about_view_GET(self):
        response = self.client.get(reverse("website:about_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/about.html')

    def test_contact_view_GET(self):
        response = self.client.get(reverse("website:about_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/about.html')

    def test_contact_view_POST_valid(self):
        pass
        # response = self.client.post(reverse('website:contact'), data={})
