from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_url(self, url: str):
        self.driver.get(url)

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))