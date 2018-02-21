from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from fitjang.views import homepage, add_data, show

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

        self.cilent.post('/', data={'activity_text': 'Mac donold' })

        self.assertEqual(Activity.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_add_data_returns_correct_html(self):
            request = HttpRequest()
            response = add_data(request)

    def test_show_returns_correct_html(self):
            request = HttpRequest()
            response = show(request)
