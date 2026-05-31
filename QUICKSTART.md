# 🎯 Quick Start Guide - GreenCity Tests

## Быстрый старт за 5 минут

### 1️⃣ Клонирование и установка

```bash
# Перейти в проект
cd greencity-tests

# Установить зависимости
pip install -r requirements.txt
```

### 2️⃣ Запуск первого теста

```bash
# Запустить все тесты
pytest -v

# Или запустить конкретный тест
pytest tests/test_events_page.py::TestEventsPageDisplay::test_events_page_loads -v
```

### 3️⃣ Просмотр результатов в Allure

```bash
# Запустить с Allure отчетом
pytest --alluredir=allure-results

# Открыть отчет
allure serve allure-results
```

---

## 📋 Структура проекта

```
greencity-tests/
├── src/pages/              # Page Objects
│   ├── base_page.py        # Базовый класс для страниц
│   └── events_page.py      # Страница с событиями
├── src/components/         # UI Components
│   ├── base_component.py   # Базовый класс для компонентов
│   ├── header.py           # Компонент Header
│   ├── filter_panel.py     # Компонент FilterPanel
│   └── event_card.py       # Компонент EventCard
├── tests/
│   └── test_events_page.py # Все тесты (7 тест-кейсов)
├── conftest.py             # Фикстури и конфигурация
├── pytest.ini              # Конфиг pytest
└── requirements.txt        # Зависимости
```

---

## ✅ Что сделано

### Архитектура
- ✅ **Page Object Model** - EventsPage, BasePage
- ✅ **Component-based** - Header, FilterPanel, EventCard
- ✅ **BaseComponent** - все компоненты наследуются от него
- ✅ **BasePage** - общие методы для всех страниц

### Тесты (7 тест-кейсов)
- ✅ Загрузка страницы событий
- ✅ Видимость заголовка
- ✅ Отображение событий
- ✅ Получение названий событий
- ✅ Клик на кнопку фильтра
- ✅ Проверка опций фильтра
- ✅ Выбор опции фильтра

### Code Quality
- ✅ **PEP8** - чистый код с правильным форматированием
- ✅ **Без sleep()** - используется WebDriverWait
- ✅ **Allure** - @allure.feature, @allure.story, @allure.step
- ✅ **Документация** - README.md с полной инструкцией

---

## 🚀 Основные команды

```bash
# Все тесты
pytest -v

# Только smoke тесты
pytest -m smoke -v

# Только regression тесты
pytest -m regression -v

# С Allure отчетом
pytest --alluredir=allure-results
allure serve allure-results

# Конкретный тест
pytest tests/test_events_page.py::TestEventsPageDisplay -v

# С подробным выводом
pytest -vv --tb=long
```

---

## 💡 Примеры кода

### Использование Page Object

```python
from src.pages import EventsPage

events_page = EventsPage(driver)
events_page.navigate_to_events()
count = events_page.get_events_count()
```

### Использование Component

```python
from src.components import Header, FilterPanel

header = Header(driver)
header.search("workshop")

filter_panel = FilterPanel(driver)
filter_panel.select_filter_option(0)
filter_panel.apply_filters()
```

### Использование в тесте с Allure

```python
import pytest
import allure

@allure.feature("Events")
@allure.story("Display")
class TestEvents:
    @allure.title("Test page loads")
    def test_page_loads(self, setup_teardown):
        with allure.step("Navigate to events"):
            self.events_page.navigate_to_events()
        
        with allure.step("Verify page loaded"):
            assert self.events_page.is_events_loaded()
```

---

## 📊 Тестовое покриття

| Класс | Тест | Маркер |
|-------|------|--------|
| TestEventsPageDisplay | test_events_page_loads | smoke |
| TestEventsPageDisplay | test_header_is_visible | smoke |
| TestEventsPageDisplay | test_events_displayed | regression |
| TestEventTitles | test_get_event_titles | regression |
| TestEventFiltering | test_filter_button_clickable | smoke |
| TestEventFiltering | test_filter_options_exist | regression |
| TestEventFiltering | test_select_filter_option | regression |

---

## 🔧 Как добавить новый тест

1. Создать класс в `tests/test_*.py`
2. Добавить фикстуру `setup` с инициализацией компонентов
3. Использовать `@allure.feature`, `@allure.story`, `@allure.title`
4. Обернуть шаги в `with allure.step()`
5. Запустить `pytest -v`

---

## 📞 Помощь и документация

- 📖 **Полная документация**: см. [README.md](README.md)
- 💻 **Примеры кода**: см. [EXAMPLES.md](EXAMPLES.md)
- 🧪 **Тесты**: см. [tests/test_events_page.py](tests/test_events_page.py)

---

**Готово! Начните писать тесты! 🚀**
