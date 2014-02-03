import unittest
from selenium import webdriver


class TestPlanalyzerRating(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def login(self):
        driver = self.driver
        with open('/tmp/credentials.txt', 'r') as fp:
            url, username, password = fp.read().split('|')
        self.driver.get(url)
        self.driver.find_element_by_id('id_username').send_keys(username)
        self.driver.find_element_by_id('id_password').send_keys(password)
        self.assertTrue('Site administration' in self.driver.title)

    def search_for_plan_admin(self, q):
        """
        Search for audit reports, then navigate to the first plan's admin page.
        @todo: implement the next plan nav
        """
        driver = self.driver
        driver.find_element_by_link_text('Audit reports').click()
        driver.find_element_by_id('searchbar').send_keys(q)
        driver.find_element_by_css_selector('input[value="Search"]').click()

    def test_planalyzer_rating(self):
        self.login()
        self.search_for_plan_admin('in out burger')

    def tearDown(self):
        pass  # intentional for now

if __name__ == '__main__':
    unittest.main()
