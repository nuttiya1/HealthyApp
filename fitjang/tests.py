from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from fitjang.views import homepage
from fitjang.models import Activity

# Create your tests here.

class HomePageTest(TestCase):
    def test_user_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_activity': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'homepage.html')

    def test_root_hotme_page(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Fit Jang</title>', html)
        # self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'homepage.html')

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Activity()
        first_item.activity_text = 'The first (ever) list item'
        first_item.save()

        second_item = Activity()
        second_item.activity_text = 'Item the second'
        second_item.save()

        saved_items = Activity.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.activity_text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.activity_text, 'Item the second')
    # def test_home_page_can_save_a_POST_request(self):
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['item_text'] = 'A new list item'
    #
    #     response = home_page(request)
    #     self.assertIn('A new list item', response.content.decode())
    # def test_can_save_a_POST_request(self):
    #
    #     self.client.get('/', data={'activity_text': 'Mac donold' })
    #     self.assertEqual(Activity.objects.count(), 1)
    #
    #     new_item = Activity.objects.first()
    #     self.assertEqual(new_item.activity_text, 'Mac donold')
