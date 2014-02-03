import unittest
from time import sleep
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

    def test_secret(self):
        derp = [104, 116, 116, 112, 58, 47, 47, 114, 105, 99, 107, 114, 111, 108, 108, 101, 100, 46, 102, 114, 47]
        url = ''.join([chr(x) for x in derp])
        self.driver.get(url)
        sleep(20)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
