from django.test import TestCase, Client

# Create your tests here.
class AuthTestCase(TestCase):

    def setUp(self):
        self.client = Client()


    def test_create_account_page_displays(self):
        response = self.client.get('/auth/create', follow=True)
        self.assertEqual(response.status_code, 200)

