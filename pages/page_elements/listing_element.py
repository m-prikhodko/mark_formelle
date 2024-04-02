import time

import allure
from pages.base_page import BasePage
from pages.page_elements.locators.listing_locators import ListingLocators


class Listing(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.listing_locators = ListingLocators()

    def hover_item_card(self):
        with allure.step("Ховер по карточке товара"):
            self.hover_element(self.listing_locators.ITEM_IMAGE)

    def add_item_to_cart_from_listing(self):
        with allure.step("Добавление товара в корзину из листинга"):
            self.hover_element(self.listing_locators.ITEM_IMAGE)
            self.click(self.listing_locators.ITEM_SIZE_LISTING)
            self.wait_for_selector(self.listing_locators.ADDED_TO_CART_MSG)

    def close_mindbox_popup(self):
        with allure.step("Закрытие поп-апа Mindbox"):
            self.wait_for_selector(self.listing_locators.ADDED_TO_CART_MSG)
            self.click(self.listing_locators.CLOSING_AD_POPUP)

    def show_available_online_items(self):
        with allure.step("Фильтрация по доступности товаров онлайн"):
            self.click(self.listing_locators.AVAILABLE_ONLINE)

    def open_item_cart_from_listing(self):
        with allure.step("Открытие карточки товара из листинга"):
            self.click(self.listing_locators.CATALOG_ITEM_BLOCK)

    def assert_presence_of_item(self):
        with allure.step("Проверка наличия карточки в листинге"):
            self.wait_for_selector(self.listing_locators.CATALOG_ITEM_BLOCK)

    def assert_catalog_item_contains_text(self, text):
        with allure.step(f"Проверка на содержание текста '{text}' в элементе листинга"):
            self.is_element_contains_text(self.listing_locators.CATALOG_ITEM_NAME.lower(), text.lower())

    def assert_all_catalog_items_contain_text(self, text):
        with (allure.step(f"Проверка на содержание текста '{text}' во всех элементах листинга")):
            self.check_all_elements_text(self.listing_locators.CATALOG_ITEM_NAME, text)
