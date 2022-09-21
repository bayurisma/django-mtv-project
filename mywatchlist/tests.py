from django.test import TestCase, Client
from django.urls import resolve

class mywatchlistTest(TestCase):
    def test_mywatchlist_url_exists(self):
        response = Client().get('mywatchlist')
        self.assertEqual(response.status_code, 200)
    
    def test_xml_url_exists(self):
        response = Client().get('xml')
        self.assertEqual(response.status_code, 200)

    def test_json_url_exists(self):
        response = Client().get('json')
        self.assertEqual(response.status_code, 200)
