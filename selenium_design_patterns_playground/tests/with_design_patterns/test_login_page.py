import unittest

from selenium import webdriver

from selenium_design_patterns_playground.pages import LoginPage


class TestLoginPage(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/example.html")

    @property
    def login_page(self) -> LoginPage:
        return LoginPage(self.driver)

    def login(self, username: str, password: str):
        login_page = self.login_page

        login_page.username.text = username
        login_page.password.text = password
        login_page.submit_button.click()

    def test_successful_login(self):
        login_page = self.login_page

        self.login('admin', 'password')
        self.assertTrue(login_page.login_status.is_logged_in)

    def test_unsuccessful_login(self):
        login_page = self.login_page

        self.login('invalid-username', 'invalid-password')
        self.assertTrue(login_page.login_status.login_failed)


if __name__ == '__main__':
    unittest.main()
