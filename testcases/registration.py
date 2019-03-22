import unittest
import objects.locators as locator
import time
from selenium.webdriver import Firefox, Chrome
import config.params as params
import random

browserList = {
    'firefox': Firefox,
    'chrome': Chrome
}

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.browser = browserList.get(params.browser)()
        self.browser.get(params.url)
        self.browser.find_element_by_css_selector(locator.signin).click()

    def test_Registration(self):
        reg_email = f'random{random.randint(1, 1000)}@gmail.com'
        user_registration = RegisterUserWithOnlyMandatoryFields('TestUser', 'User', reg_email, 'password', '6th Main',
                                                                'Indianapolis', 'Indiana', '46204', 'United States',
                                                                '9192634580', 'test account')
        user_registration.register(self.browser)
        self.browser.find_element_by_id(locator.submit_register).click()

    def test_Registration_with_additional_fields(self):
        reg_email = f'random{random.randint(1, 1000)}@gmail.com'
        user_registration = RegisterUserWithAdditionalFields('TestUser', 'User', reg_email, 'password', '6th Main',
                                                             'Indianapolis', 'Indiana', '46204', 'United States',
                                                             '9192634580', 'test account', 'Techno Logic')
        user_registration.register(self.browser)
        self.browser.find_element_by_id(locator.submit_register).click()

    def tearDown(self):
        self.browser.find_element_by_css_selector(locator.logout).click()
        self.browser.close()
        self.browser.quit()


class RegisterUserWithOnlyMandatoryFields(object):
    def __init__(self, first_name, last_name, email, password, address, city, state, zip, country, mobile, alias):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
        self.mobile = mobile
        self.alias = alias

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


class RegisterUserWithAdditionalFields(RegisterUserWithOnlyMandatoryFields):
    def __init__(self,first_name, last_name, email, password, address, city, state, zip, country, mobile, alias, company):
        self.company = company
        RegisterUserWithOnlyMandatoryFields.__init__(self, first_name, last_name, email, password, address, city, state, zip, country, mobile, alias)

    def register(self, browser):
        RegisterUserWithOnlyMandatoryFields.register(self, browser)
        browser.find_element_by_id(locator.company).send_keys(self.company)
        time.sleep(15)


if __name__ == '__main__':
    unittest.main()