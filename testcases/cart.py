import unittest
import objects.locators as locator
import time
import random
from selenium.webdriver import Firefox, Chrome
import config.params as params

browserList = {
    'firefox': Firefox,
    'chrome': Chrome
}


class TestCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = browserList.get(params.browser)()
        cls.browser.set_window_size(1024, 1366)
        time.sleep(5)
        cls.browser.get(params.url)

        cls.browser.find_element_by_css_selector(locator.signin).click()
    #     cls.browser.find_element_by_id(locator.email).send_keys(params.username)
    #     cls.browser.find_element_by_id(locator.password).send_keys(params.password)
    #     cls.browser.find_element_by_id(locator.submit).click()
    #
    # def test_ValidLogin(self):
    #     self.assertEqual(self.browser.find_element_by_css_selector(locator.account).text, 'Jyothy Mariam John')
    #
    # def test_EmptyCart(self):
    #     self.assertEqual(self.browser.find_element_by_css_selector(locator.cart_empty).text, '')
    #
    # def test_AddToCart(self):
    #     self.browser.find_element_by_id('search_query_top').send_keys('Faded Short Sleeve T-shirts')
    #     self.browser.find_element_by_name('submit_search').click()
    #     self.browser.find_element_by_css_selector('.icon-th-list').click()
    #     self.browser.find_element_by_css_selector('.ajax_add_to_cart_button').click()
    #     time.sleep(5)
    #     self.browser.find_element_by_css_selector('.continue').click()
    #     self.assertEqual(self.browser.find_element_by_css_selector(locator.cart_quantity).text, '1')

    # def test_Registration(self):
    #     userRegistration = RegisterUserWithOnlyMandatoryFields("TestUser", "Users", "random300@gmail.com", "anything")
    #     userRegistration.register(self.browser)

    def test_Registration(self):
        regEmail = f'random{random.randint(1,1000)}@gmail.com'
        userRegistration = RegisterUserWithOnlyMandatoryFields("TestUser", "Users", regEmail, "anything")
        userRegistration.register(self.browser)



    # @classmethod
    # def tearDownClass(cls):
    #     cls.browser.find_element_by_css_selector(locator.logout).click()
    #     cls.browser.close()
    #     cls.browser.quit()


class RegisterUserWithOnlyMandatoryFields:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.address = '6th Main'
        self.city = 'xyz'
        self.state = 'Indiana'
        self.zip = '46204'
        self.country = 'United States'
        self.mobile = '9192634580'
        self.alias = 'test account'

    def register(self, browser):
        browser.find_element_by_id(locator.email).send_keys(self.email)
        browser.find_element_by_id(locator.submit_create).click()
        time.sleep(5)
        browser.find_element_by_id(locator.first_name).send_keys(self.first_name)
        browser.find_element_by_id(locator.last_name).send_keys(self.last_name)
        browser.find_element_by_id(locator.password).send_keys(self.password)
        browser.find_element_by_id(locator.address).send_keys(self.address)
        browser.find_element_by_id(locator.city).send_keys(self.city)
        browser.find_element_by_id(locator.state).send_keys(self.state)
        browser.find_element_by_id(locator.zip).send_keys(self.zip)
        browser.find_element_by_id(locator.country).send_keys(self.country)
        browser.find_element_by_id(locator.mobile).send_keys(self.mobile)

        browser.find_element_by_id(locator.submit_register).click()


class RegisterUserWithAdditionalFields(RegisterUserWithOnlyMandatoryFields):
    def __init__(self):
        self.company = 'Techno Logic'

    def register(self, browser):
        browser.find_element_by_id(locator.company).sendlkeys(self.company)


if __name__ == '__main__':
    unittest.main()
