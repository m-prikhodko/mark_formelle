import allure
from pages.base_page import BasePage
from pages.locators.search_locators import SearchLocators


class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_locators = SearchLocators()

    def assert_search_request_is_in_field(self, search_request):
        with allure.step(f"Проверка наличия поискового запроса {search_request} в поле поиска"):
            self.assert_element_attribute(self.search_locators.SEARCH_INPUT, 'value', search_request)
