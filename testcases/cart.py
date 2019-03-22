import unittest
import objects.locators as locator
import time
from selenium.webdriver import Firefox, Chrome
import config.params as params


class TestCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if params.browser == 'firefox':
            cls.browser = Firefox()
        elif params.browser == 'chrome':
            cls.browser = Chrome()

        cls.browser.get(params.url)

        cls.browser.find_element_by_css_selector(locator.signin).click()
        cls.browser.find_element_by_id(locator.email_sign_in).send_keys(params.username)
        cls.browser.find_element_by_id(locator.password_sign_in).send_keys(params.password)
        cls.browser.find_element_by_id(locator.submit).click()

    def test_ValidLogin(self):
        self.assertEqual(self.browser.find_element_by_css_selector(locator.account).text, 'Jyothy Mariam John')

    def test_EmptyCart(self):
        self.assertEqual(self.browser.find_element_by_css_selector(locator.cart_empty).text, '')

    def test_AddToCart(self):
        self.browser.find_element_by_id('search_query_top').send_keys('Faded Short Sleeve T-shirts')
        self.browser.find_element_by_name('submit_search').click()
        self.browser.find_element_by_css_selector('.icon-th-list').click()
        self.browser.find_element_by_css_selector('.ajax_add_to_cart_button').click()
        time.sleep(5)
        self.browser.find_element_by_css_selector('.continue').click()
        self.assertEqual(self.browser.find_element_by_css_selector(locator.cart_quantity).text, '1')

    @classmethod
    def tearDownClass(cls):
        cls.browser.find_element_by_css_selector(locator.logout).click()
        cls.browser.close()
        cls.browser.quit()


if __name__ == '__main__':
    unittest.main()
