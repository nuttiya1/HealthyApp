from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
       self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows_text = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows_text])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Ploy has heard about a cool new online health app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention web-app name
        self.assertIn('Fit Jang', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Fit Jang', header_text)
        time.sleep(2)

        # She decide to look up to these available link
        # She saw 'วิธีวิธีการออกกำลังกาย' and decide to click it
        self.browser.find_element_by_link_text('วิธีการออกกำลังกาย').click()
        time.sleep(2)

        # She saw 'ท่าออกกำลังกายส่วนอก' and decide to click it
        self.browser.find_element_by_link_text('ท่าออกกำลังกายส่วนอก').click()
        time.sleep(2)
        # and went back to exercise sections
        self.browser.find_element_by_id('back_home_exercise').click()
        time.sleep(2)

        # She saw 'ท่าออกกำลังกายส่วนหลัง' and decide to click it
        self.browser.find_element_by_link_text('ท่าออกกำลังกายส่วนหลัง').click()
        time.sleep(2)
        # and went back to exercise sections
        self.browser.find_element_by_id('back_home_exercise').click()
        time.sleep(2)

        # She saw 'ท่าออกกำลังกายส่วนแขน' and decide to click it
        self.browser.find_element_by_link_text('ท่าออกกำลังกายส่วนแขน').click()
        time.sleep(2)
        # and went back to exercise sections
        self.browser.find_element_by_id('back_home_exercise').click()
        time.sleep(2)

        # She saw 'ท่าออกกำลังกายส่วนไหล่' and decide to click it
        self.browser.find_element_by_link_text('ท่าออกกำลังกายส่วนไหล่').click()
        time.sleep(2)
        # and went back to exercise sections
        self.browser.find_element_by_id('back_home_exercise').click()
        time.sleep(2)

        # She saw 'ท่าออกกำลังกายส่วนขา' and decide to click it
        self.browser.find_element_by_link_text('ท่าออกกำลังกายส่วนขา').click()
        time.sleep(2)
        # and went back to exercise sections
        self.browser.find_element_by_id('back_home_exercise').click()
        time.sleep(2)
        # she go back to homepage
        self.browser.find_element_by_id('back_home').click()
        time.sleep(2)

        # She saw 'แนะนำอาหาร' and decide to click it
        self.browser.find_element_by_link_text('แนะนำอาหาร').click()
        time.sleep(2)
        # she went back to homepage
        self.browser.find_element_by_id('back_home').click()
        time.sleep(2)

        # Now she felt more excite about this app
        # she has no hesitate to explore more feature of this amazing app
        # she began to record her recent activity
        # she was jogging about 2 hours

        # she select an available activity which match with her recently
        el = self.browser.find_element_by_id('id_of_select')
        for option in el.find_elements_by_tag_name('option'):
           if option.text == 'Jogging':
              option.click()
              break
        time.sleep(1)

        # She has to insert her secret info to this app
        # but it doesn't to her
        inputWeight = self.browser.find_element_by_id('id_weight')
        inputWeight.send_keys(60)
        time.sleep(1)
        # She might seem overweight but she's pretty tall

        # Now she insert the jogging time
        inputTime = self.browser.find_element_by_id('id_time')
        inputTime.send_keys(120)
        time.sleep(1)

        # She click 'submit'
        self.browser.find_element_by_id("id_sub").click()
        self.browser.get('http://localhost:8000')
        time.sleep(3)

        # After she click sumbit, she check data in table
        # She has been recall that this is not collect data
        # She insert a wrong number (she was a model could it that be)
        # She see wrong data in line 1
        # She click delete button in line "1"
        self.browser.find_element_by_id('1').click()
        time.sleep(3)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
