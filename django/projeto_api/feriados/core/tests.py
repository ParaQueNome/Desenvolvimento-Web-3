from django.test import TestCase

# Create your tests here.

class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    def test_texto(self):
        self.assertContains(self.resp,'Natal')

class IndependenciaTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/independencia')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_texto(self):
        self.assertContains(self.resp,'Independencia')
        self.assertContains(self.resp,'morte')

class TiradentesTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/tiradentes')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_texto(self):
        self.assertContains(self.resp,'Tiradentes')
        



    