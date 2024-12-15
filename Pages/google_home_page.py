from selenium.webdriver.common.by import By
from .base_page import BasePage

class GoogleHomePage(BasePage):
    SEARCH_BOX = (By.NAME, "q")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.go_to_url("https://www.google.co.kr")

    def search(self, keyword: str):
        search_box = self.wait_for_element_visible(self.SEARCH_BOX)
        search_box.send_keys(keyword)
        search_box.submit()