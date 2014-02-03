import unittest
from selenium import webdriver


class TestDuckDuckGo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_duck_duck_go(self):
        driver = self.driver
        driver.get('http://www.duckduckgo.com')

        # search for bacon
        search_box = driver.find_element_by_id('search_form_input_homepage')
        search_box.send_keys('bacon')
        driver.find_element_by_id('search_button_homepage').click()

        # look for a description
        self.assertTrue('Bacon is a cured meat prepared from a pig' in driver.find_element_by_tag_name('body').text)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
