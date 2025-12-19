from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MoviePage(BasePage):
    MOVIE_TITLE = (By.TAG_NAME, "h1")
    TRAILER_BUTTON = (By.XPATH, "//span[contains(text(), 'Трейлер')]")

    def is_movie_opened(self) -> bool:
        return self.find(*self.MOVIE_TITLE).is_displayed()

    def is_trailer_available(self) -> bool:
        return self.find(*self.TRAILER_BUTTON).is_displayed()
