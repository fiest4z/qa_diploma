import allure
import pytest

from pages.main_page import MainPage
from pages.movie_page import MoviePage
from config.settings import BASE_URL


@allure.title("Поиск фильма по точному названию")
@allure.story("Поиск")
@pytest.mark.ui
def test_search_movie_by_exact_name(driver) -> None:
    main_page = MainPage(driver)
    movie_page = MoviePage(driver)

    with allure.step("Открыть главную страницу"):
        main_page.open(BASE_URL)

    with allure.step("Ввести название фильма и нажать Enter"):
        main_page.search_movie("Титаник")

    with allure.step("Проверить, что открылась карточка фильма"):
        assert movie_page.is_movie_opened()


@allure.title("Проверка доступности трейлера в карточке фильма")
@allure.story("Карточка фильма")
@pytest.mark.ui
def test_trailer_availability(driver) -> None:
    main_page = MainPage(driver)
    movie_page = MoviePage(driver)

    with allure.step("Открыть карточку фильма"):
        main_page.open(BASE_URL)
        main_page.search_movie("Титаник")

    with allure.step("Проверить наличие кнопки трейлера"):
        assert movie_page.is_trailer_available()



@allure.title("Поиск фильма с пустым полем")
@allure.story("Поиск")
@pytest.mark.ui
def test_search_with_empty_input(driver) -> None:
    main_page = MainPage(driver)

    with allure.step("Открыть главную страницу"):
        main_page.open(BASE_URL)

    with allure.step("Нажать Enter с пустым полем"):
        main_page.search_movie("")

    with allure.step("Проверить, что произошёл переход на другую страницу"):
        assert "kinopoisk.ru" in driver.current_url



@allure.title("Поиск фильма со спецсимволами")
@allure.story("Поиск")
@pytest.mark.ui
def test_search_movie_with_special_characters(driver) -> None:
    main_page = MainPage(driver)
    movie_page = MoviePage(driver)

    with allure.step("Выполнить поиск фильма '1+1'"):
        main_page.open(BASE_URL)
        main_page.search_movie("1+1")

    with allure.step("Проверить, что карточка фильма открылась"):
        assert movie_page.is_movie_opened()


@allure.title("Поиск несуществующего фильма")
@allure.story("Поиск")
@pytest.mark.ui
def test_search_nonexistent_movie(driver) -> None:
    main_page = MainPage(driver)

    with allure.step("Выполнить поиск несуществующего фильма"):
        main_page.open(BASE_URL)
        main_page.search_movie("1254689")

    with allure.step("Проверить отображение страницы без результатов"):
        assert "search" in driver.current_url
