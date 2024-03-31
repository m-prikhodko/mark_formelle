# Mark Formelle Autotests

Проект предназначен для тестирования веб-приложения интернет-магазина Mark Formelle с помощью pytest и Playwright.

## Установка

1. Склонируйте репозиторий на свой компьютер.
2. Установите необходимые зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Использование

1. Запустите нужные тесты через Allure:

    ```bash
    pytest --alluredir=result tests/[test-file].py
    ```
   
   Запуск одного теста из файла:

   ```bash
    pytest --alluredir=result tests/[test-file].py -k [test_title]
    ```

2. Сгенерируйте и откройте Allure-report для просмотра отчета по результатам тестирования:

   ```bash
    allure serve result
    ```


## Структура проекта

- `tests/`: Директория со всеми автотестами.
- `pages/`: Описание действий со страницами, элементами и их локаторы.
- `data/`: Данные для тестов (URLs, выбор браузера / браузеров и т.п.).
- `utils/`: Файлы со вспомогательными методами для тестирования.
- `conftest.py`: Фикстуры для запуска тестов.
- `.env`: Описание окружения (разрешение экрана) и определение параметра запуска Headless.
- `requirements.txt`: Список зависимостей, используемых в данном проекте.
- `.gitignore`: Папки и файлы, которые не должны идти в Git.

## Вклад в проект

Если вы хотите внести свой вклад в проект, следуйте инструкциям:

1. Форкните репозиторий.
2. Создайте новую ветку: `git checkout -b feature/my-feature`.
3. Внесите изменения и сделайте коммиты: `git commit -m "Add my feature"`.
4. Запушьте изменения: `git push origin feature/my-feature`.
5. Создайте Pull Request.
