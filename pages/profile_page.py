import time

import allure
from pages.base_page import BasePage
from pages.locators.profile_locators import ProfileLocators
from pages.page_elements.locators.header_locators import HeaderLocators
from pages.page_elements.header_element import Header


class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.profile_locators = ProfileLocators()
        self.header_locators = HeaderLocators()
        self.header = Header

    def cancel_order_from_profile(self):
        with allure.step("Отмена заказа через кнопку 'Отменить заказ' в ЛК пользователя"):
            self.click(self.profile_locators.CANCEL_ORDER_BTN)
            self.is_element_visible(self.profile_locators.CANCEL_ORDER_BLOCK)
            self.click(self.profile_locators.CONFIRM_CANCEL_ORDER)
            self.check_url('https://markformelle.by/personal/order/', timeout=180000)
            self.assert_element_hidden(self.profile_locators.CANCEL_ORDER_BTN)
