# 🌱 GreenCity Tests - Test Automation Framework

Проєкт автоматизації тестування веб-сайту GreenCity з використанням **Page Object Model (POM)** та **Component-based архітектури**.

## 📋 Про проєкт

Це фреймворк для автоматизації тестування UI GreenCity з фокусом на:
- ✅ **POM (Page Object Model)** - чистий код та легка підтримка
- ✅ **Component-based approach** - компоненти, що повторно використовуються
- ✅ **Allure Reports** - детальні звіти про тести
- ✅ **Best Practices** - PEP8, чіткі очікування, відсутність sleep

---

## 🏗️ Архітектура Проекту

```
greencity-tests/
├── src/
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── base_page.py           # Базовий клас для всіх сторінок
│   │   └── events_page.py         # Page Object для сторінки подій
│   └── components/
│       ├── __init__.py
│       ├── base_component.py      # Базовий клас для всіх компонентів
│       ├── header.py              # Компонент Header
│       ├── filter_panel.py        # Компонент FilterPanel
│       └── event_card.py          # Компонент EventCard
├── tests/
│   ├── __init__.py
│   └── test_events_page.py        # Тести для сторінки подій
├── conftest.py                     # Pytest фікстури та конфигурація
├── pytest.ini                      # Конфігурация pytest
├── requirements.txt                # Залежності проєкта
└── README.md                       # Цей файл
```

---

## ⚙️ Встановлення та налаштування

### 1. Вимоги
- **Python 3.8+**
- **pip** (менеджер пакетов Python)

### 2. Установка зависимостей

```bash
# Встановити всі залежності з requirements.txt
pip install -r requirements.txt
```

**Основные зависимости:**
- `selenium==4.15.2` - WebDriver automation
- `pytest==7.4.3` - Test framework
- `allure-pytest==2.13.2` - Allure reporting
- `webdriver-manager==4.0.1` - Автоматичне керування драйверами

### 3. Конфигурация переменных окружения (опционально)

Створіть файл `.env` в корені проєкту:

```bash
BASE_URL=https://greencity.com
HEADLESS_MODE=false
IMPLICIT_WAIT=10
```

---

## 🚀 Запуск Тестів

### Базовий запуск всіх тестів

```bash
pytest
```

### Запуск с verbose режимом

```bash
pytest -v
```

### Запуск конкретного файла с тестами

```bash
pytest tests/test_events_page.py -v
```

### Запуск конкретного теста

```bash
pytest tests/test_events_page.py::TestEventsPageDisplay::test_events_page_loads -v
```

### Запуск тестов по маркерам

```bash
# Только smoke тесты
pytest -m smoke -v

# Только regression тесты
pytest -m regression -v

# Все кроме smoke
pytest -m "not smoke" -v
```

### Запуск с генерацией Allure отчета

```bash
# Запустить тесты с Allure
pytest --alluredir=allure-results

# Просмотреть Allure отчет
allure serve allure-results
```

---

## 📊 Генерирование Allure Отчета

### Установка Allure (один раз)

**На Windows (с Chocolatey):**
```bash
choco install allure
```

**На Linux/Mac (с Homebrew):**
```bash
brew install allure
```

### Просмотр Отчета

```bash
# Запустить тесты и создать отчет
pytest --alluredir=allure-results

# Открыть отчет в браузере
allure serve allure-results
```

---

## 🧪 Тестовое Покриття

### Реализованные тест-кейсы:

#### **TestEventsPageDisplay** (Display & Navigation)
1. ✅ `test_events_page_loads` - Загрузка страницы событий
2. ✅ `test_header_is_visible` - Видимость заголовка
3. ✅ `test_events_displayed` - Отображение событий

#### **TestEventTitles** (Event Titles)
4. ✅ `test_get_event_titles` - Получение названий событий

#### **TestEventFiltering** (Filtering)
5. ✅ `test_filter_button_clickable` - Клик на кнопку фильтра
6. ✅ `test_filter_options_exist` - Доступные опции фильтра
7. ✅ `test_select_filter_option` - Выбор опции фильтра

**Статистика:**
- Всего тестов: **7**
- Smoke тесты: **3**
- Regression тесты: **4**

---

## 🏛️ Структура Кода

### BasePage (src/pages/base_page.py)

```python
class BasePage:
    """Базовый класс для всех страниц с общими методами"""
    
    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)
    
    # Методы взаимодействия с элементами
    def find_element(self, locator)
    def click_element(self, locator)
    def input_text(self, locator, text)
    def is_element_visible(self, locator)
    # и другие...
```

### BaseComponent (src/components/base_component.py)

```python
class BaseComponent:
    """Базовый класс для всех компонентов"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Те же методы что и в BasePage
    # Все компоненты наследуют этот класс
```

### EventsPage (src/pages/events_page.py)

```python
class EventsPage(BasePage):
    """Page Object для страницы событий"""
    
    def navigate_to_events(self)
    def get_events_count(self) -> int
    def get_event_titles(self) -> list
    def click_filter_button(self)
    def is_events_loaded(self) -> bool
```

### Header Component (src/components/header.py)

```python
class Header(BaseComponent):
    """Компонент Header для навигации"""
    
    def click_logo(self)
    def is_header_visible(self) -> bool
    def search(self, query: str)
```

### FilterPanel Component (src/components/filter_panel.py)

```python
class FilterPanel(BaseComponent):
    """Компонент FilterPanel для фильтрации"""
    
    def is_filter_panel_visible(self) -> bool
    def get_filter_options_count(self) -> int
    def select_filter_option(self, option_index: int) -> bool
    def apply_filters(self)
    def reset_filters(self)
```

---

## 🎯 Best Practices Применены

✅ **PEP8 Compliance** - Чистый код с правильным форматированием

✅ **No time.sleep()** - Используется WebDriverWait для явных ожиданий

✅ **POM + Components** - Разделение на страницы и компоненты

✅ **BaseComponent** - Все компоненты наследуют базовый класс

✅ **Allure Reporting** - Детальные отчеты с аннотациями

✅ **DRY Principle** - Отсутствие дублирования кода

---

## 🔧 Разработка Новых Тестов

### Пример добавления нового теста:

```python
import pytest
import allure
from src.pages import EventsPage
from src.components import Header

@allure.feature("Events")
@allure.story("Search")
class TestEventSearch:
    
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.events_page = EventsPage(self.driver)
    
    @allure.title("Test event search")
    @pytest.mark.regression
    def test_search_event(self):
        with allure.step("Navigate to events"):
            self.events_page.navigate_to_events()
        
        with allure.step("Search for event"):
            header = Header(self.driver)
            header.search("workshop")
        
        with allure.step("Verify results"):
            results = self.events_page.get_events_count()
            assert results > 0, "No search results found"
```

---

## 📝 Добавление Новых Компонентов

```python
# src/components/pagination.py
from .base_component import BaseComponent
from selenium.webdriver.common.by import By

class Pagination(BaseComponent):
    """Компонент пагинации"""
    
    NEXT_BUTTON = (By.CSS_SELECTOR, "[class*='next']")
    PREV_BUTTON = (By.CSS_SELECTOR, "[class*='prev']")
    
    def click_next(self):
        self.click_element(self.NEXT_BUTTON)
    
    def click_prev(self):
        self.click_element(self.PREV_BUTTON)
```

Затем добавить в `src/components/__init__.py`:
```python
from .pagination import Pagination
__all__ = [..., 'Pagination']
```

---

## 🐛 Troubleshooting

### Проблема: WebDriver не скачался

**Решение:** `webdriver-manager` должен скачать его автоматически. Если нет:
```bash
pip install --upgrade webdriver-manager
```

### Проблема: Тесты не находят элементы

**Решение:**
1. Проверьте CSS селекторы в locators
2. Увеличьте timeout в `conftest.py` (по умолчанию 10 сек)
3. Используйте `is_element_visible()` перед взаимодействием

### Проблема: Allure отчет не генерируется

**Решение:**
```bash
# Убедитесь что allure установлен
allure --version

# Переустановите если нужно
pip install allure-pytest --upgrade
```

---

## 📞 Контакты и Поддержка

Для вопросов или проблем:
- Проверьте документацию выше
- Посмотрите на примеры тестов в `tests/test_events_page.py`
- Обратитесь к разработчику

---

## 🚀 Краткая Шпаргалка

```bash
# Установка
pip install -r requirements.txt

# Все тесты
pytest -v

# Только smoke
pytest -m smoke -v

# С Allure отчетом
pytest --alluredir=allure-results
allure serve allure-results

# Конкретный тест
pytest tests/test_events_page.py::TestEventsPageDisplay::test_events_page_loads -v
```
