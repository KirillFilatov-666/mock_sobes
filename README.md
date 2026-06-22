# mock_sobes — учебный AQA-фреймворк

![tests](https://github.com/KirillFilatov-666/mock_sobes/actions/workflows/tests.yml/badge.svg)

Учебный фреймворк автоматизации тестирования: **pytest + Selenium (Page Object) + requests + Allure + CI**.
UI-тесты гоняются на [the-internet.herokuapp.com](https://the-internet.herokuapp.com/login),
API-тесты — на [jsonplaceholder](https://jsonplaceholder.typicode.com/).

## 🧰 Стек
- **UI-тесты:** Selenium WebDriver, паттерн Page Object Model
- **API-тесты:** requests
- **Тест-раннер:** pytest (фикстуры, параметризация, маркеры)
- **Отчёты:** Allure (с автоскриншотом при падении UI-теста)
- **Параллельный запуск:** pytest-xdist
- **CI:** GitHub Actions (на каждый push/PR)
- **Контейнеризация:** Docker + docker-compose (Selenium в отдельном контейнере)

## 📁 Структура
```
mock_sobes/
├── pages/                  # Page Objects (слой "как взаимодействуем со страницей")
│   ├── base_page.py        # общие методы: find, click, type, ожидания
│   ├── login_page.py
│   └── secure_page.py
├── tests/
│   ├── ui/                 # UI-тесты (через Page Object)
│   └── api/                # API-тесты
├── conftest.py             # фикстуры (driver, api) + хук скриншота при падении
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .github/workflows/      # CI
```

## 🚀 Запуск локально
```bash
python -m venv venv
venv\Scripts\activate              # Windows
pip install -r requirements.txt

pytest -v                          # все тесты
pytest tests/api -v                # только API
pytest tests/ui -v                 # только UI
pytest -n auto                     # параллельно
HEADLESS=true pytest tests/ui      # UI без окна браузера
```

## 📊 Allure-отчёт
```bash
pytest --alluredir=allure-results
allure serve allure-results        # требуется установленный Allure CLI
```

## 🐳 Запуск в Docker
Поднимает Selenium в отдельном контейнере и прогоняет все тесты:
```bash
docker compose up --build
```

