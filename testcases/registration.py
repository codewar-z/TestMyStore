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
        user = RegistrationFactory.user('partial')
        user.register(self.browser)
        self.browser.find_element_by_id(locator.submit_register).click()

    def test_Registration_with_additional_fields(self):
        user = RegistrationFactory.user('full')
        user.register(self.browser)
        self.browser.find_element_by_id(locator.submit_register).click()

    def tearDown(self):
        self.browser.find_element_by_css_selector(locator.logout).click()
        self.browser.close()
        self.browser.quit()


class RegistrationFactory:
    @staticmethod
    def user(registration_type):
        reg_email = f'random{random.randint(1, 1000)}@gmail.com'
        if registration_type == 'partial':
            return User("TestUser", "User", reg_email, "password")
        return UserWithAdditionalField("TestUser", "User", reg_email, "password")


class User(object):
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


class UserWithAdditionalField(User):
    def __init__(self,first_name, last_name, email, password):
        self.company = 'Techno Logic'
        User.__init__(self, first_name, last_name, email, password)

    def register(self, browser):
        User.register(self, browser)
        browser.find_element_by_id(locator.company).send_keys(self.company)


if __name__ == '__main__':
    unittest.main()
