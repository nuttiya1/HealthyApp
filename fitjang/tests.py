from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from fitjang.views import homepage
from fitjang.models import Activity,Weight,Time

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
        response = self.client.post('/', data={'item_activity': 'A new list item', 'val_weight': 0, 'val_time': 0})
        self.assertEqual(Activity.objects.count(), 1)
        new_item = Activity.objects.first()
        self.assertEqual(new_item.activity_text, 'A new list item')

        self.assertEqual(Weight.objects.count(), 1)
        val_weigth = Weight.objects.first()
        self.assertEqual(val_weigth.weight_data, 0)

        self.assertEqual(Time.objects.count(), 1)
        val_time = Time.objects.first()
        self.assertEqual(val_time.amount_of_time, 0)

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_activity': 'A new list item', 'val_weight': 0, 'val_time': 0})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_displays_all_list_items(self):
        Activity.objects.create(activity_text='itemey 1')
        Weight.objects.create(weight_data=0)
        Time.objects.create(amount_of_time=0)
        # Activity.objects.create(activity_text='itemey 2')

        response = self.client.get('/')

        self.assertIn('itemey 1', response.content.decode())
        #self.assertIn(0, response.content.decode())
        #self.assertIn(0, response.content.decode())
        # self.assertIn('itemey 2', response.content.decode())

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

class ActivityModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Activity(activity_text='The first (ever) list item')
        first_item.save()

        All_items = Activity.objects.all()
        self.assertEqual(All_items.count(), 1)

        self.assertEqual(All_items[0].activity_text, 'The first (ever) list item')

class WeigthModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_weight = Weight(weight_data=60)
        first_weight.save()

        All_weight = Weight.objects.all()
        self.assertEqual(All_weight.count(), 1)

        self.assertEqual(All_weight[0].weight_data, 60)

class TimeModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_time = Time(amount_of_time=120)
        first_time.save()

        All_time = Time.objects.all()
        self.assertEqual(All_time.count(), 1)

        self.assertEqual(All_time[0].amount_of_time, 120)
