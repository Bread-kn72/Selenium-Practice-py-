from .base_page import BasePage

class GoogleResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_back(self):
        self.driver.back()