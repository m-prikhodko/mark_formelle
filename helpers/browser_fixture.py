import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Запуск Chrome/Chromium
        # browser = p.firefox.launch(headless=False)  # Запуск Firefox
        # browser = p.webkit.launch(headless=False)  # Запуск WebKit
        yield browser
        browser.close()
