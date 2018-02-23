# from django.template.loader import render_to_string
from django.test import TestCase
# from django.http import HttpRequest
from django.urls import resolve
from fitjang.views import homepage
from fitjang.models import Activity

# Create your tests here.

class HomePageTest(TestCase):
    def test_user_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

    def test_root_hotme_page(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Fit Jang</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'homepage.html')

    # def test_can_save_a_POST_request(self):
    #
    #     self.client.get('/', data={'activity_text': 'Mac donold' })
    #     self.assertEqual(Activity.objects.count(), 1)
    #
    #     new_item = Activity.objects.first()
    #     self.assertEqual(new_item.activity_text, 'Mac donold')
