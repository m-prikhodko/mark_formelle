import allure
from pages.base_page import BasePage
from pages.locators.search_locators import SearchLocators


class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_locators = SearchLocators()
