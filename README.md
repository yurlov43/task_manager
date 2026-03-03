```markdown
# Task Manager — консольное приложение для управления списком дел

Простое консольное приложение для управления задачами с сохранением в JSON-файл.

## Функционал

- Добавить задачу
- Удалить задачу
- Отметить задачу выполненной
- Показать список задач
- Автоматическое сохранение в `tasks.json`

## Зависимости

```bash
pip install -r requirements.txt
```

## Запуск приложения

```bash
python main.py
```

## Структура проекта

```
task-manager/
├── models/
│   ├── __init__.py
│   └── task.py              # Pydantic модель задачи
├── repositories/
│   ├── __init__.py
│   └── task_repository.py   # Работа с JSON-файлом
├── services/
│   ├── __init__.py
│   └── task_service.py      # Бизнес-логика
├── presentation/
│   ├── __init__.py
│   └── console_app.py       # Консольный интерфейс
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Общие фикстуры для тестов
│   ├── test_models.py
│   ├── test_repositories.py
│   ├── test_services.py
│   └── test_integration.py
├── requirements.txt         # Зависимости для запуска
├── requirements-dev.txt     # Зависимости для разработки
├── main.py                  # Точка входа
└── README.md
```

## Тестирование

### Зависимости для тестов

```bash
pip install -r requirements-dev.txt
```

### Запуск тестов

```bash
# Запустить все тесты
pytest -v

# С покрытием кода
pytest --cov=. --cov-report=term
```

### Структура тестов

- `test_models.py` — тесты модели Task
- `test_repositories.py` — тесты работы с JSON
- `test_services.py` — тесты бизнес-логики
- `test_integration.py` — сквозной тест всего приложения

## Лицензия

MIT
```