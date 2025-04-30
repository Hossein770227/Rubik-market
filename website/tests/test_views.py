from django.test import TestCase , Client

class Test_AboutView(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_about_view_GET(self):
        response = self.client.get("website:about-us")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/about.html')



