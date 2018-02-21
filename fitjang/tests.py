from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from fitjang.views import homepage, show
from fitjang.models import Activity

# Create your tests here.

class HomePageTest(TestCase):
    def test_root_hotme_page(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = homepage(request)
        #self.assertTrue(response.content.startswith(b'<html>'))
        #self.assertTrue(response.content.endswith(b'</html>'))

    def test_can_save_a_POST_request(self):

        self.client.get('/', data={'activity_text': 'Mac donold' })
        self.assertEqual(Activity.objects.count(), 1)

        #new_item = Activity.objects.first()
        #self.assertEqual(new_item.activity_text, 'Mac donold')
