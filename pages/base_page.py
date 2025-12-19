from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, by: By, locator: str):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by: By, locator: str) -> None:
        self.find(by, locator).click()

    def type(self, by: By, locator: str, text: str) -> None:
        element = self.find(by, locator)
        element.clear()
        element.send_keys(text)
