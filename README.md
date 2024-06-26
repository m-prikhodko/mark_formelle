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
   
3. В Tear down конкретного теста в Allure можно скачать его трассировку.
После скачивания необходимо перетащить zip-архив в открытую страницу https://trace.playwright.dev/ в браузере.



## Структура проекта

- `tests/`: Директория со всеми автотестами.
- `pages/`: Описание действий со страницами, элементами и их локаторы.
- `data/`: Данные для тестов (URLs).
- `utils/`: Файлы со вспомогательными методами для тестирования.
- `conftest.py`: Фикстура для запуска тестов. Здесь можно задать браузер / браузеры для запуска, режим запуска (headless / headed), разрешение экрана.
- `requirements.txt`: Список зависимостей, используемых в данном проекте.
- `.gitignore`: Папки и файлы, которые не должны идти в Git.

## Вклад в проект

Если вы хотите внести свой вклад в проект, следуйте инструкциям:

1. Форкните репозиторий.
2. Создайте новую ветку: `git checkout -b feature/my-feature`.
3. Внесите изменения и сделайте коммиты: `git commit -m "Add my feature"`.
4. Запушьте изменения: `git push origin feature/my-feature`.
5. Создайте Pull Request.
