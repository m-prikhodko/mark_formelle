import allure
from pages.base_page import BasePage
from pages.page_elements.locators.cookie_popup_locators import CookieLocators


class CookiePopup(BasePage):
    def __init__(self, page):
        self.page = page
        super().__init__(page)
        self.cookie_locators = CookieLocators()

    def assert_cookie_popup_is_present(self):
        with allure.step("Проверка наличия поп-апа куки на странице"):
            self.is_element_present(self.cookie_locators.COOKIE_POPUP_BY)