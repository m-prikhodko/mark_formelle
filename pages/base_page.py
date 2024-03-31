import allure
from playwright.sync_api import Page, expect
from data.urls import BASE_URL_BY


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self._BASE_URL_BY = BASE_URL_BY
        self._endpoint = ""

    @property
    def page_url(self):
        return self._BASE_URL_BY + self._endpoint

    @page_url.setter
    def page_url(self, endpoint):
        self._endpoint = endpoint

    def navigate(self, url):
        with allure.step(f"Переход на URL: {url}"):
            self.page.goto(url)

    def check_url(self, expected_url):
        with allure.step(f"Проверка URL: ожидаемый URL - {expected_url}"):
            expect(self.page).to_have_url(expected_url)

    def wait_for_url_change(self, expected_url):
        with allure.step(f"Ожидание изменения URL на {expected_url}"):
            self.page.wait_for_url(expected_url)

    def wait_for_page_load(self):
        with allure.step("Ожидание загрузки страницы"):
            self.page.wait_for_load_state('load')

    def click(self, selector):
        with allure.step(f"Клик по элементу: {selector}"):
            self.page.click(selector)

    def hover_element(self, selector):
        with allure.step(f"Ховер элемента: {selector}"):
            self.page.hover(selector)
            self.page.wait_for_selector(selector)

    def press_enter(self, selector):
        with allure.step(f"Нажатие Enter для: {selector}"):
            self.page.press(selector, 'Enter')

    def is_element_visible(self, selector):
        with allure.step(f"Проверка видимости элемента: {selector}"):
            expect(self.page.locator(selector)).to_be_visible()

    def is_button_active(self, selector):
        with allure.step(f"Проверка активности кнопки: {selector}"):
            expect(self.page.locator(selector)).to_be_enabled()

    def is_element_contains_text(self, selector, text):
        with allure.step(f"Проверка на содержание текста '{text}' в элементе '{selector}'"):
            expect(self.page.locator(selector)).to_contain_text(text)

    def check_all_elements_text(self, selector, text):
        with allure.step(f"Проверка на содержание текста '{text}' во всех элементах '{selector}'"):
            elements = self.page.locator(selector).all()
            for element in elements:
                actual_text = element.text_content()
                with allure.step(f"Проверка, что текст '{text.lower()}' содержится в '{actual_text.lower()}'"):
                    assert text.lower() in actual_text.lower()

    def input_text(self, selector, text):
        with allure.step(f"Ввод текста '{text}' в элемент: '{selector}'"):
            self.page.fill(selector, text)

    def input_filtered_text(self, selector, text):
        with allure.step(f"Ввод текста 'FILTERED' в элемент: {selector}"):
            self.page.fill(selector, text)

    def wait_for_selector(self, selector):
        with allure.step(f"Ожидание появления элемента: {selector}"):
            self.page.wait_for_selector(selector, state='visible')

    def wait_for_disappear_selector(self, selector):
        with allure.step(f"Ожидание исчезновения элемента: {selector}"):
            self.page.wait_for_selector(selector, state='detached')

    def assert_text_present_on_page(self, text):
        with allure.step(f"Проверка наличия текста '{text}' на странице"):
            expect(self.page).to_have_text(text)

    def assert_text_present_in_element(self, selector, text):
        with allure.step(f"Проверка наличия текста '{text}' в элементе {selector}"):
            expect(self.page.locator(selector)).to_have_text(text)

    def assert_element_attribute(self, selector, attribute, value):
        with allure.step(f"Проверка значения '{value}' атрибута '{attribute}' элемента '{selector}'"):
            expect(self.page.locator(selector)).to_have_attribute(attribute, value)

    def assert_element_hidden(self, selector):
        with allure.step(f"Проверка на скрытие элемента '{selector}'"):
            expect(self.page.locator(selector)).to_be_hidden()

    def assert_element_has_value(self, selector, value):
        with allure.step(f"Проверка на содержание значения '{value}' в элементе '{selector}'"):
            expect(self.page.locator(selector)).to_have_value(value)
