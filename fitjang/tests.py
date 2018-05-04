from django.template.loader import render_to_string
from django.test import TestCase
from django.test import Client
from django.http import HttpRequest
from django.urls import resolve
from fitjang.views import homepage
from fitjang.models import Activity, Mets
# Create your tests here.

class HomePageTest(TestCase):
    def test_user_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Activity.objects.count(), 0)
        # self.assertEqual(Weight.objects.count(), 0)
        # self.assertEqual(Time.objects.count(), 0)

    def test_can_save_a_POST_request(self):
        # Add table in test database
        Mets.objects.create(name="Run", value=7.0)

        response = self.client.post('/addActivity', data={
        'item_activity': 'Run', 'val_weight': 100, 'val_time':120})

        self.assertEqual(Activity.objects.count(), 1)
        new_item = Activity.objects.first()

        self.assertEqual(new_item.activity_text, 'Run')

    def test_can_delete_with_a_POST_request(self):
        # Add table at the very first begining
        # Due the different database
        Mets.objects.create(name="Run", value=7.0)
        response = self.client.post('/addActivity', data={
        'item_activity': 'Run', 'val_weight': 100, 'val_time':120})

        response = self.client.post('/deleteActivity', data={'del_id' : Activity.objects.first().id})
        
        self.assertIsNone(Activity.objects.first())

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
