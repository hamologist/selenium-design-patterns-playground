import unittest

from selenium import webdriver


class TestLoginPage(unittest.TestCase):

    def test_successful_login(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/example.html")

        username = driver.find_element_by_id('username-input')
        username.send_keys('admin')

        password = driver.find_element_by_id('password-input')
        password.send_keys('password')

        submit = driver.find_element_by_id('submit-button')
        submit.click()

        login_status = driver.find_element_by_id('test-status')
        self.assertEqual(login_status.text, 'Authenticated')

    def test_unsuccessful_login(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/example.html")

        username = driver.find_element_by_id('username-input')
        username.send_keys('incorrect-username')

        password = driver.find_element_by_id('password-input')
        password.send_keys('incorrect-password')

        submit = driver.find_element_by_id('submit-button')
        submit.click()

        login_status = driver.find_element_by_id('test-status')
        self.assertEqual(login_status.text, 'Failed')


if __name__ == '__main__':
    unittest.main()
