from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
       self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows_text = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows_text])
        # row_weigth = table.find_elements_by_tag_name('tr')
        # self.assertIn(row_weigth, [row.text for row in row_weigth])
        # row_time = table.find_elements_by_tag_name('tr')
        # self.assertIn(row_time, [row.text for row in row_time])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online health app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention web-app name
        self.assertIn('Fit Jang', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Fit Jang', header_text)

        # She is invited to enter an activity straight away
        inputbox = self.browser.find_element_by_id('id_new_activity')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a Fit Jang activity'
        )

        # She types "Run" into a text box (Edith's hobby)
        #
        inputbox.send_keys('Run')
        time.sleep(2)
        inputWeight = self.browser.find_element_by_id('id_weight')
        inputWeight.send_keys(60)
        time.sleep(2)
        inputTime = self.browser.find_element_by_id('id_time')
        inputTime.send_keys(120)
        time.sleep(2)
        self.browser.find_element_by_id("id_sub").click()
        time.sleep(2)

        self.check_for_row_in_list_table('1: Run 60 กก. 120 นาที')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        # inputbox = self.browser.find_element_by_id('id_new_activity')
        # inputbox.send_keys('Wetgth')
        # time.sleep(2)
        # inputWeigth = self.browser.find_element_by_id('id_weigth')
        # inputWeigth.send_keys(65)
        # time.sleep(2)
        # inputTime = self.browser.find_element_by_id('id_time')
        # inputTime.send_keys(60)
        # time.sleep(2)
        # self.browser.find_element_by_id("id_sub").click()
        # time.sleep(2)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Run 60 กก. 120 นาที')
        # self.check_for_row_in_list_table('2: Wetgth')

        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

if __name__ == '__main__':
    unittest.main(warnings='ignore')
