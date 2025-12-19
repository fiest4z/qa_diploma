from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    SEARCH_INPUT = (By.NAME, "kp_query")

    def open(self, url: str) -> None:
        self.driver.get(url)

    def search_movie(self, movie_name: str) -> None:
        self.type(*self.SEARCH_INPUT, movie_name)
        self.find(*self.SEARCH_INPUT).send_keys("\n")
