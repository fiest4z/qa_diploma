import allure
import pytest

from api.base_api import BaseAPI
from config.settings import API_URL, SEARCH_ENDPOINT
from config.credentials import API_TOKEN, INVALID_API_TOKEN


@allure.title("Поиск фильма по названию на кириллице")
@allure.story("API: поиск фильмов")
@pytest.mark.api
def test_search_movie_cyrillic() -> None:
    api = BaseAPI(API_URL, API_TOKEN)

    with allure.step("Отправить GET-запрос с кириллическим названием"):
        response = api.get(SEARCH_ENDPOINT, params={"query": "Титаник"})

    with allure.step("Проверить код ответа"):
        assert response.status_code == 200

    with allure.step("Проверить, что результат не пустой"):
        data = response.json()
        assert data["docs"]


@allure.title("Поиск фильма по названию на латинице")
@allure.story("API: поиск фильмов")
@pytest.mark.api
def test_search_movie_latin() -> None:
    api = BaseAPI(API_URL, API_TOKEN)

    response = api.get(SEARCH_ENDPOINT, params={"query": "Lord of the Rings"})

    assert response.status_code == 200
    assert response.json()["docs"]


@allure.title("Поиск фильма по названию с цифрами")
@allure.story("API: поиск фильмов")
@pytest.mark.api
def test_search_movie_numbers() -> None:
    api = BaseAPI(API_URL, API_TOKEN)

    response = api.get(SEARCH_ENDPOINT, params={"query": "2012"})

    assert response.status_code == 200
    assert response.json()["docs"]


@allure.title("Поиск фильма с произвольным набором символов")
@allure.story("API: негативные сценарии")
@pytest.mark.api
def test_search_movie_random_symbols() -> None:
    api = BaseAPI(API_URL, API_TOKEN)

    response = api.get(SEARCH_ENDPOINT, params={"query": "!@#$%"})

    assert response.status_code == 200
    assert "docs" in response.json()
    assert isinstance(response.json()["docs"], list)


@allure.title("Поиск фильма с пустым полем")
@allure.story("API: негативные сценарии")
@pytest.mark.api
def test_search_movie_empty_query() -> None:
    api = BaseAPI(API_URL, API_TOKEN)

    response = api.get(SEARCH_ENDPOINT)

    assert response.status_code == 200
    assert response.json()["docs"]


@allure.title("Поиск фильма без токена")
@allure.story("API: авторизация")
@pytest.mark.api
def test_search_without_token() -> None:
    api = BaseAPI(API_URL)

    response = api.get(SEARCH_ENDPOINT, params={"query": "Титаник"})

    assert response.status_code == 401


@allure.title("Поиск фильма с неактуальным токеном")
@allure.story("API: авторизация")
@pytest.mark.api
def test_search_with_invalid_token() -> None:
    api = BaseAPI(API_URL, INVALID_API_TOKEN)

    response = api.get(SEARCH_ENDPOINT, params={"query": "Титаник"})

    assert response.status_code == 401


@allure.title("Поиск фильма с неверным HTTP-методом")
@allure.story("API: негативные сценарии")
@pytest.mark.api
def test_search_with_invalid_method() -> None:
    api = BaseAPI(API_URL, API_TOKEN)

    response = api.put(SEARCH_ENDPOINT, params={"query": "Титаник"})

    assert response.status_code == 404
