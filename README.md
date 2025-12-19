## Описание проекта
Данный проект содержит автоматизированные тесты для сайта [Кинопоиск](https://www.kinopoisk.ru/) на основе финальной работы по ручному тестированию.  
Проект включает:
- UI-тесты (Selenium) для проверки основных сценариев поиска и работы с карточкой фильма.
- API-тесты (requests) для проверки поиска фильмов через публичный API Kinopoisk.

> **Важно:** При запуске UI-тестов на реальном сайте может появляться CAPTCHA, что делает автоматизацию нестабильной. Для стабильного запуска рекомендуется тестовое окружение или мок-страницы.

Проект полностью соответствует PEP8 и использует современный стек для тестирования: `pytest`, `allure`, `selenium`, `requests`.

Ссылка на финальный проект по ручному тестированию: [ссылка на финальный проект]()


---

## Установка

1. Клонируем репозиторий:
```bash
git clone https://github.com/your_username/qa_diploma.git
cd qa_diploma
```
2. Создаем виртуальное окружение и активируем:
```bash
python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\activate       # Windows
```
3. Устанавливаем зависимости:
```bash
pip install -r requirements.txt
```


### Переменные окружения

Для запуска API-тестов необходимо задать переменную окружения:

KINOPOISK_API_TOKEN — API-токен сервиса kinopoisk.dev

Токен не хранится в репозитории по соображениям безопасности.

### Запуск тестов

API-тесты:
```bash
pytest -m "api" -v
```

UI-тесты:
```bash
pytest -m "ui" -v
```

Все тесты:
```bash
pytest -v
```

Allure отчет:

```bash
pytest -m "api" --alluredir=allure-results
allure serve allure-results
```


### Ссылка на финальный проект:
```html
https://mikhailskypro.yonote.ru/doc/kursovaya-rabota-finalnye-proekt-po-ruchnomu-testirovaniyu-d9PVsWuJEu
```
