from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
       self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('Fit Jang', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Fit Jang', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_activity')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a Fit Jang activity'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Run')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Run', [row.text for row in rows])

        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

if __name__ == '__main__':
    unittest.main(warnings='ignore')
