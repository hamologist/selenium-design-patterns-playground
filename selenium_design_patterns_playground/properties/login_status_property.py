from selenium_design_patterns.page_property import PageProperty


class LoginStatusProperty(PageProperty):

    @property
    def is_logged_in(self):
        return self.element.text == 'Authenticated'

    @property
    def login_failed(self):
        return self.element.text == 'Failed'
