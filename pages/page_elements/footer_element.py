import allure
from pages.base_page import BasePage
from pages.page_elements.locators.footer_locators import FooterLocators


class Footer(BasePage):
    def __init__(self, page):
        self.page = page
        super().__init__(page)
        self.footer_locators = FooterLocators()

    def assert_for_byers_is_present(self):
        with allure.step("Проверка наличия блока 'Покупателям' в футере"):
            self.is_element_visible(self.footer_locators.FOR_BUYERS_BLOCK)
