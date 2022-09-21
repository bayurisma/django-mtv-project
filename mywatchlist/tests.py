from django.test import TestCase, Client
from django.urls import resolve

class mywatchlistTest(TestCase):
    def test_html_url_exists(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def test_xml_url_exists(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_json_url_exists(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
