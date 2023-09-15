from django.test import TestCase

# Create your tests here.

class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    def test_texto(self):
        self.assertContains(self.resp,'natal')

class Independencia(TestCase):
    def setUp(self):
        self.resp = self.client.get('/independencia')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    
    def text_texto(self):
        self.assertContains(self.resp,'Independencia')
        self.assertContains(self.resp,'morte')