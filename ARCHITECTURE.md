# 🏗️ Architecture Overview - GreenCity Tests

## Общая архитектура

```
┌─────────────────────────────────────────────────────────┐
│                    TESTS (Test Cases)                    │
│  test_events_page.py                                     │
│  ├── TestEventsPageDisplay                              │
│  ├── TestEventTitles                                    │
│  └── TestEventFiltering                                 │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│              PAGES (Page Objects)                        │
│  EventsPage (наследует BasePage)                        │
│  ├── navigate_to_events()                               │
│  ├── get_events_count()                                 │
│  ├── get_event_titles()                                 │
│  ├── click_filter_button()                              │
│  └── is_events_loaded()                                 │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│            COMPONENTS (UI Components)                    │
│  Header, FilterPanel, EventCard                          │
│  (все наследуют BaseComponent)                           │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│         BASE CLASSES (Shared Functionality)              │
│  BasePage ─────────────────── BaseComponent             │
│  • find_element()            • find_element()           │
│  • click_element()           • click_element()          │
│  • input_text()              • input_text()             │
│  • get_element_text()        • get_element_text()       │
│  • scroll_to_element()       • scroll_to_element()      │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│              SELENIUM WEBDRIVER                          │
│  Управление браузером и элементами                      │
└─────────────────────────────────────────────────────────┘
```

---

## 🎯 Design Patterns Использованные

### 1. Page Object Model (POM)

**Цель:** Инкапсулировать логику страницы отдельно от тестов

```python
# ✅ ПРАВИЛЬНО - использование POM
class EventsPage(BasePage):
    def get_events_count(self):
        return len(self.find_elements(self.EVENT_CARDS))

# Тест просто вызывает методы страницы
events_count = events_page.get_events_count()
assert events_count > 0
```

**Преимущества:**
- Легко обновлять селекторы (в одном месте)
- Тесты читаемые и не зависят от HTML
- Переиспользование кода

### 2. Component-based Architecture

**Цель:** Выделить переиспользуемые UI элементы в отдельные классы

```python
# Каждый компонент отвечает за один элемент UI
class Header(BaseComponent):
    def search(self, query):
        self.input_text(self.SEARCH_INPUT, query)

class FilterPanel(BaseComponent):
    def select_filter_option(self, index):
        options = self.find_elements(self.FILTER_OPTIONS)
        if index < len(options):
            options[index].click()

# Использование в Page Object
class EventsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)
        self.filter_panel = FilterPanel(driver)
```

**Преимущества:**
- DRY (Don't Repeat Yourself)
- Компоненты переиспользуются в разных страницах
- Сосредоточенная ответственность

### 3. Base Classes (Template Method Pattern)

**Цель:** Предоставить общие методы для работы с элементами

```python
class BaseComponent:
    """Содержит общие методы для всех компонентов"""
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

class Header(BaseComponent):
    """Наследует все методы из BaseComponent"""
    def search(self, query):
        self.input_text(self.SEARCH_INPUT, query)  # Из BaseComponent
```

---

## 📁 Структура файлов

### `src/pages/`

```
pages/
├── __init__.py
├── base_page.py          # Базовый класс для всех страниц
│   └── class BasePage:
│       • navigate_to()
│       • find_element()
│       • click_element()
│       • input_text()
│       • get_element_text()
│       • is_element_visible()
│       • scroll_to_element()
│
└── events_page.py        # Специфичная страница
    └── class EventsPage(BasePage):
        • navigate_to_events()
        • get_events_count()
        • get_event_titles()
        • click_filter_button()
        • is_events_loaded()
```

### `src/components/`

```
components/
├── __init__.py
├── base_component.py     # Базовый класс для компонентов
│   └── class BaseComponent:
│       • find_element()
│       • click_element()
│       • input_text()
│       • get_element_text()
│       • is_element_visible()
│       • scroll_to_element()
│       • get_element_count()
│
├── header.py             # Компонент навигации
│   └── class Header(BaseComponent):
│       • click_logo()
│       • is_header_visible()
│       • search()
│
├── filter_panel.py       # Компонент фильтрации
│   └── class FilterPanel(BaseComponent):
│       • is_filter_panel_visible()
│       • get_filter_options_count()
│       • select_filter_option()
│       • apply_filters()
│       • reset_filters()
│
└── event_card.py         # Компонент карточки события
    └── class EventCard:
        • get_title()
        • get_date()
        • get_location()
        • click_card()
        • click_button()
```

### `tests/`

```
tests/
├── __init__.py
└── test_events_page.py
    ├── TestEventsPageDisplay
    │   ├── test_events_page_loads()
    │   ├── test_header_is_visible()
    │   └── test_events_displayed()
    ├── TestEventTitles
    │   └── test_get_event_titles()
    └── TestEventFiltering
        ├── test_filter_button_clickable()
        ├── test_filter_options_exist()
        └── test_select_filter_option()
```

---

## 🔄 Workflow - Как работает тест

```
1. Test запускается
   └─> setup() фикстура инициализирует драйвер и компоненты
       
2. Тест вызывает методы Page Object
   └─> EventsPage.navigate_to_events()
       
3. Page Object вызывает методы компонентов (если нужны)
   └─> Header.search(query)
       
4. Компоненты (или Page Object) используют WebDriver через BasePage/BaseComponent
   └─> self.click_element(locator)
       └─> WebDriverWait для явного ожидания элемента
       
5. Результаты проверяются в assert
   └─> assert events_page.is_events_loaded()
   
6. Allure записывает шаги и результаты
   └─> @allure.step() фиксирует каждый шаг
   
7. После теста run teardown()
   └─> Очищаются cookies, закрывается браузер
```

---

## 🛠️ Как добавить новый Page Object

### Пример: Создание страницы для профиля

```python
# src/pages/profile_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProfilePage(BasePage):
    """Profile Page Object"""
    
    # Locators
    USER_NAME = (By.CSS_SELECTOR, "[class*='user-name']")
    EDIT_BUTTON = (By.CSS_SELECTOR, "[class*='edit-btn']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[class*='logout-btn']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = f"{self.base_url}/profile"
    
    def navigate_to_profile(self):
        self.navigate_to(self.page_url)
    
    def get_user_name(self) -> str:
        return self.get_element_text(self.USER_NAME)
    
    def click_edit_button(self):
        self.click_element(self.EDIT_BUTTON)
    
    def logout(self):
        self.click_element(self.LOGOUT_BUTTON)
```

### Добавить в `src/pages/__init__.py`

```python
from .base_page import BasePage
from .events_page import EventsPage
from .profile_page import ProfilePage  # ← Добавить

__all__ = ['BasePage', 'EventsPage', 'ProfilePage']
```

---

## 🛠️ Как добавить новый Component

### Пример: Создание компонента Pagination

```python
# src/components/pagination.py
from selenium.webdriver.common.by import By
from .base_component import BaseComponent

class Pagination(BaseComponent):
    """Pagination Component"""
    
    NEXT_BUTTON = (By.CSS_SELECTOR, "[class*='next']")
    PREV_BUTTON = (By.CSS_SELECTOR, "[class*='prev']")
    CURRENT_PAGE = (By.CSS_SELECTOR, "[class*='current-page']")
    
    def click_next(self):
        self.click_element(self.NEXT_BUTTON)
    
    def click_prev(self):
        self.click_element(self.PREV_BUTTON)
    
    def get_current_page(self) -> str:
        return self.get_element_text(self.CURRENT_PAGE)
```

### Добавить в `src/components/__init__.py`

```python
from .pagination import Pagination  # ← Добавить

__all__ = ['BaseComponent', 'Header', 'FilterPanel', 'EventCard', 'Pagination']
```

---

## 📊 Зависимости классов

```
test_events_page.py
    ├── uses: EventsPage
    │   └── extends: BasePage
    │       ├── uses: WebDriverWait
    │       └── uses: selenium
    │
    ├── uses: Header
    │   └── extends: BaseComponent
    │       └── uses: WebDriverWait
    │
    └── uses: FilterPanel
        └── extends: BaseComponent
            └── uses: WebDriverWait
```

---

## ✨ Best Practices

1. **Не используйте time.sleep()**
   ```python
   # ❌ BAD
   time.sleep(5)
   element = driver.find_element(...)
   
   # ✅ GOOD
   element = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.ID, "element"))
   )
   ```

2. **Используйте локаторы как константы**
   ```python
   # ❌ BAD
   def click_button(self):
       self.driver.find_element(By.CSS_SELECTOR, "[class*='btn']").click()
   
   # ✅ GOOD
   BUTTON = (By.CSS_SELECTOR, "[class*='btn']")
   def click_button(self):
       self.click_element(self.BUTTON)
   ```

3. **Создавайте описательные имена методов**
   ```python
   # ❌ BAD
   def get_count(self):
       pass
   
   # ✅ GOOD
   def get_events_count(self) -> int:
       pass
   ```

4. **Документируйте методы**
   ```python
   def get_events_count(self) -> int:
       """
       Get count of event cards on page.
       
       Returns:
           Count of event cards
       """
       return len(self.find_elements(self.EVENT_CARDS))
   ```

---

## 📈 Scalability

Проект легко масштабируется:

1. **Добавление новых страниц** - просто создать новый класс наследующий BasePage
2. **Добавление новых компонентов** - просто создать новый класс наследующий BaseComponent
3. **Добавление новых тестов** - просто добавить новый метод в класс TestXXX
4. **Добавление новых тест-файлов** - просто создать новый файл test_*.py

Вся архитектура готова для расширения! 🚀
