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
        driver.find_element_by_id('result_list').find_element_by_tag_name('tbody').find_element_by_tag_name('a').click()

    def get_planalyzer_rating_link(self):
        """
        The link text is the BrightScope rating rounded to 0.1.
        """
        driver = self.driver
        driver.find_element_by_link_text('View Planalyzer').click()
        driver.switch_to_window(driver.window_handles[-1])
        link = driver.find_element_by_id('planalyzer-rating').find_element_by_tag_name('a')
        return link

    def test_planalyzer_rating(self):
        self.login()
        self.search_for_plan_admin('in out burger')

        # get rating from planalyzer
        pl_link = self.get_planalyzer_rating_link()
        pl_rating = float(pl_link.text)

        # get rating from rating page
        pl_link.click()
        self.assertTrue('401k Rating' in self.driver.title)
        rp_rating = int(self.driver.find_element_by_id('your_plan_rating').text)

        # compare ratings
        self.assertTrue(abs(pl_rating - rp_rating) <= 0.5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
