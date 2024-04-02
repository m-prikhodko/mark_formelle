import allure
from pages.base_page import BasePage
from pages.page_elements.locators.cookie_popup_locators import CookieLocators


class CookiePopup(BasePage):
    def __init__(self, page):
        self.page = page
        super().__init__(page)
        self.cookie_locators = CookieLocators()

    def reject_cookie_by(self):
        with allure.step("Отклонение куки BY"):
            self.is_element_visible(self.cookie_locators.COOKIE_POPUP_BY)
            self.click(self.cookie_locators.COOKIE_REJECT_BTN_BY)
            self.assert_element_hidden(self.cookie_locators.COOKIE_POPUP_HIDDEN_BY)
