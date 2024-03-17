import allure
from pages.base_page import BasePage
from pages.page_elements.locators.header_locators import HeaderLocators


class Header(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.header_locators = HeaderLocators()

    def check_infoline_text(self, text):
        with allure.step(f"Проверка текста {text} в инфополосе в хедере"):
            self.assert_text_present_in_element(self.header_locators.INFOLINE, text)

    def close_infoline(self):
        with allure.step("Закрытие инфополосы в хедере"):
            self.click_button(self.header_locators.INFOLINE_CLOSE)

    def open_catalog(self):
        with allure.step("Открытие каталога"):
            self.click_button(self.header_locators.CATALOG)

    def go_to_all_for_women(self):
        with allure.step("Переход в листинг 'Смотреть все' для женщин"):
            self.click_button(self.header_locators.OPEN_ALL_FOR_WOMEN)

    def go_to_stores_page(self):
        with allure.step("Открытие страницы 'Магазины' из хедера"):
            self.click_button(self.header_locators.STORES_HEADER)

    def open_location_popup(self):
        with allure.step("Открытие поп-апа выбора локации из хедера"):
            self.click_button(self.header_locators.LOCATION_HEADER)

    def is_go_home_clickable(self):
        with allure.step("Проверка на кликабельность кнопки домой"):
            return self.is_button_active(self.header_locators.LOGO)

    def go_home(self):
        with allure.step("Переход на главную кликом на лого в хедере"):
            self.click_button(self.header_locators.LOGO)

    def open_search(self):
        with allure.step("Открытие поиска в хедере"):
            self.click_button(self.header_locators.SEARCH)

    def popular_search_requests_present(self):
        with allure.step("Проверка присутствия популярных поисковых запросов в поиске"):
            return self.is_element_present(self.header_locators.SEARCH_POPULAR)

    def input_into_search(self, search_request):
        with allure.step(f"Ввод текста {search_request} в поисковую строку"):
            self.input_text(self.header_locators.SEARCH_FIELD, search_request)

    def press_enter_in_search_field(self):
        with allure.step("Отправка поискового запроса нажатием Enter"):
            self.press_enter(self.header_locators.SEARCH_FIELD)

    def click_search_button(self):
        with allure.step("Отправка поискового запроса кликом на кнопку"):
            self.click_button(self.header_locators.SEARCH_SUBMIT_BTN)

    def close_search_with_cross(self):
        with allure.step("Закрытие поисковой строки в хедере кликом на крестик"):
            self.click_button(self.header_locators.SEARCH_CLOSE)

    def close_search_with_search_icon(self):
        with allure.step("Закрытие поисковой строки в хедере кликом на иконку поиска"):
            self.click_button(self.header_locators.SEARCH)

    def send_search_request(self, search_request):
        with allure.step(f"Отправка поискового запроса для {search_request}"):
            self.open_search()
            self.input_into_search(search_request)
            self.press_enter_in_search_field()

    def open_login_popup(self):
        with allure.step("Открытие поп-апа логина из хедера"):
            self.click_button(self.header_locators.PROFILE_HEADER)

    def open_favorites(self):
        with allure.step("Открытие Избранного"):
            self.click_button(self.header_locators.FAVORITES)

    def open_cart(self):
        with allure.step("Открытие корзины из хедера"):
            self.click_button(self.header_locators.CART_HEADER)
