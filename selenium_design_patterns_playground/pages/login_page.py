from selenium_design_patterns.page_object_model.page import Page
from selenium_design_patterns.page_property import PageProperty
from selenium_design_patterns.page_property.common_properties import TextInputProperty
from selenium_design_patterns_playground.properties import LoginStatusProperty


class LoginPage(Page):

    @property
    def username(self) -> TextInputProperty:
        return TextInputProperty(self.driver, self.driver.find_element_by_id('username-input'))

    @property
    def password(self) -> TextInputProperty:
        return TextInputProperty(self.driver, self.driver.find_element_by_id('password-input'))

    @property
    def submit_button(self) -> PageProperty:
        return PageProperty(self.driver, self.driver.find_element_by_id('submit-button'))

    @property
    def login_status(self) -> LoginStatusProperty:
        return LoginStatusProperty(self.driver, self.driver.find_element_by_id('test-status'))
