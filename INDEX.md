# 📑 GreenCity Tests - Documentation Index

Полный каталог документации и указатель по всем файлам проекта.

---

## 📚 Документация

### 🚀 Для Начинающих

1. **[QUICKSTART.md](QUICKSTART.md)** ⭐ **НАЧНИТЕ ОТСЮДА**
   - 5-минутный старт
   - Основные команды
   - Первый тест
   - **Читайте, если:** Вы впервые в проекте

2. **[README.md](README.md)**
   - Полная документация
   - Все возможности
   - Troubleshooting
   - Шпаргалка по командам
   - **Читайте, если:** Нужна полная информация

### 🏗️ Для Разработчиков

3. **[ARCHITECTURE.md](ARCHITECTURE.md)**
   - Описание архитектуры
   - Design patterns
   - Как добавить новый компонент
   - Структура файлов
   - **Читайте, если:** Разрабатываете новые тесты

4. **[EXAMPLES.md](EXAMPLES.md)**
   - Примеры кода
   - Как использовать Page Objects
   - Как использовать Components
   - Примеры тестов
   - **Читайте, если:** Нужны примеры

### ✅ Статус Проекта

5. **[COMPLETION_REPORT.md](COMPLETION_REPORT.md)**
   - Отчет о завершении
   - Что было реализовано
   - Метрики проекта
   - Проверка требований
   - **Читайте, если:** Нужна полная информация о статусе

---

## 🔧 Конфигурационные Файлы

### Pytest & Allure

- **pytest.ini** - Конфигурация pytest
  - Маркеры для тестов
  - Allure options
  - Paths для тестов

- **conftest.py** - Pytest фикстуры
  - Browser fixture
  - Setup/teardown
  - Implicit waits

### Environment

- **.env** - Переменные окружения
  - BASE_URL
  - HEADLESS_MODE
  - IMPLICIT_WAIT

- **requirements.txt** - Зависимости проекта
  - Selenium
  - Pytest
  - Allure
  - WebDriver Manager

- **setup.cfg** - Метаинформация проекта
- **.gitignore** - Git ignore правила

---

## 📁 Исходный Код (src/)

### Pages (Page Object Model)

```
src/pages/
├── base_page.py
│   └── BasePage - базовый класс для всех страниц
│       • navigate_to()
│       • find_element()
│       • click_element()
│       • input_text()
│       • get_element_text()
│       • is_element_visible()
│       • scroll_to_element()
│
└── events_page.py
    └── EventsPage(BasePage) - страница с событиями
        • navigate_to_events()
        • get_events_count()
        • get_event_titles()
        • click_filter_button()
        • is_events_loaded()
```

### Components (Reusable UI Components)

```
src/components/
├── base_component.py
│   └── BaseComponent - базовый класс для компонентов
│       • find_element()
│       • click_element()
│       • input_text()
│       • get_element_text()
│       • is_element_visible()
│       • scroll_to_element()
│       • get_element_count()
│
├── header.py
│   └── Header(BaseComponent) - компонент заголовка
│       • click_logo()
│       • is_header_visible()
│       • search()
│
├── filter_panel.py
│   └── FilterPanel(BaseComponent) - компонент фильтра
│       • is_filter_panel_visible()
│       • get_filter_options_count()
│       • select_filter_option()
│       • apply_filters()
│       • reset_filters()
│
└── event_card.py
    └── EventCard - компонент карточки события
        • get_title()
        • get_date()
        • get_location()
        • click_card()
        • click_button()
```

---

## 🧪 Тесты (tests/)

### test_events_page.py - 7 тест-кейсов

#### TestEventsPageDisplay (3 теста)
```
├── test_events_page_loads [smoke]
│   └── Проверяет загрузку страницы событий
├── test_header_is_visible [smoke]
│   └── Проверяет видимость заголовка
└── test_events_displayed [regression]
    └── Проверяет отображение событий
```

#### TestEventTitles (1 тест)
```
└── test_get_event_titles [regression]
    └── Проверяет получение названий событий
```

#### TestEventFiltering (3 теста)
```
├── test_filter_button_clickable [smoke]
│   └── Проверяет клик на кнопку фильтра
├── test_filter_options_exist [regression]
│   └── Проверяет наличие опций фильтра
└── test_select_filter_option [regression]
    └── Проверяет выбор опции фильтра
```

---

## ⚡ Быстрые Команды

### Установка
```bash
pip install -r requirements.txt
```

### Запуск Тестов
```bash
pytest -v                           # Все тесты
pytest -m smoke -v                  # Только smoke
pytest -m regression -v             # Только regression
pytest -k test_events_page_loads    # По имени
```

### Allure Отчеты
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

### Проверка Конфига
```bash
python verify_config.py
python PROJECT_STATUS.py
```

---

## 🎯 Навигация по Типам Документации

### Я хочу...

#### 🚀 Быстро начать работу
→ Читайте [QUICKSTART.md](QUICKSTART.md)

#### 📖 Полную документацию
→ Читайте [README.md](README.md)

#### 🏗️ Понять архитектуру
→ Читайте [ARCHITECTURE.md](ARCHITECTURE.md)

#### 💻 Увидеть примеры кода
→ Читайте [EXAMPLES.md](EXAMPLES.md)

#### ✅ Проверить статус проекта
→ Читайте [COMPLETION_REPORT.md](COMPLETION_REPORT.md)

#### 🔧 Понять структуру проекта
→ Смотрите этот файл [INDEX.md](INDEX.md)

#### ⚙️ Разобраться с конфигом
→ Смотрите [conftest.py](conftest.py) и [pytest.ini](pytest.ini)

---

## 📊 Структура Проекта

```
greencity-tests/
│
├── 📚 Документация
│   ├── INDEX.md (этот файл)
│   ├── QUICKSTART.md
│   ├── README.md
│   ├── ARCHITECTURE.md
│   ├── EXAMPLES.md
│   └── COMPLETION_REPORT.md
│
├── 🔧 Конфигурация
│   ├── conftest.py
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── setup.cfg
│   ├── .env
│   └── .gitignore
│
├── 💻 Исходный Код
│   └── src/
│       ├── pages/
│       │   ├── base_page.py
│       │   └── events_page.py
│       └── components/
│           ├── base_component.py
│           ├── header.py
│           ├── filter_panel.py
│           └── event_card.py
│
├── 🧪 Тесты
│   └── tests/
│       └── test_events_page.py
│
└── 🔍 Валидация
    ├── PROJECT_STATUS.py
    └── verify_config.py
```

---

## 📌 Важные Моменты

### ✅ ЭТО СДЕЛАНО

- ✅ Page Object Model (POM)
- ✅ Component-based архитектура
- ✅ BaseComponent для всех компонентов
- ✅ 7 тест-кейсов (мин. 3 требовалось)
- ✅ Allure интеграция
- ✅ PEP8 code style
- ✅ Нет time.sleep()
- ✅ WebDriverWait используется
- ✅ Полная документация

### 🎯 МОЖНО РАСШИРИТЬ

- Добавить новые Page Objects
- Добавить новые Components
- Добавить новые Тесты
- Добавить параметризацию тестов
- Добавить CI/CD интеграцию
- Добавить видео записи тестов

---

## 🚀 Первые Шаги

### Если вы в первый раз:

1. Прочитайте [QUICKSTART.md](QUICKSTART.md) (5 минут)
2. Установите зависимости: `pip install -r requirements.txt`
3. Запустите тесты: `pytest -v`
4. Генерируйте отчет: `pytest --alluredir=allure-results && allure serve allure-results`
5. Изучите код в `src/`
6. Смотрите примеры в [EXAMPLES.md](EXAMPLES.md)
7. Прочитайте полный [README.md](README.md)

### Если вы разработчик:

1. Прочитайте [ARCHITECTURE.md](ARCHITECTURE.md)
2. Посмотрите структуру `src/pages/` и `src/components/`
3. Смотрите примеры в `tests/test_events_page.py`
4. Изучите `conftest.py` для фикстур
5. Смотрите [EXAMPLES.md](EXAMPLES.md) для новых компонентов

---

## 📞 Справка

| Вопрос | Ответ |
|--------|-------|
| С чего начать? | [QUICKSTART.md](QUICKSTART.md) |
| Как запустить тесты? | [README.md](README.md) - Раздел "Запуск" |
| Как написать новый тест? | [EXAMPLES.md](EXAMPLES.md) |
| Как добавить компонент? | [ARCHITECTURE.md](ARCHITECTURE.md) |
| Что было сделано? | [COMPLETION_REPORT.md](COMPLETION_REPORT.md) |
| Какова структура? | [INDEX.md](INDEX.md) - этот файл |

---

## 💡 Полезные Файлы для Быстрого Поиска

| Файл | Назначение |
|------|-----------|
| conftest.py | Браузер фикстура |
| pytest.ini | Маркеры и опции |
| src/pages/base_page.py | Базовые методы для страниц |
| src/components/base_component.py | Базовые методы для компонентов |
| tests/test_events_page.py | Все тесты с Allure |
| EXAMPLES.md | Примеры использования |

---

**Документация готова к использованию! 📚**

*Последнее обновление: May 2026*
