import allure

from pages.locators.profile_locators import ProfileLocators
from utils.date_util import get_day_after_tomorrow
from pages.base_page import BasePage
from pages.locators.cart_locators import CartLocators
from pages.page_elements.locators.header_locators import HeaderLocators
from pages.page_elements.header_element import Header


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_locators = CartLocators()
        self.header_locators = HeaderLocators()
        self.profile_locators = ProfileLocators()
        self.header = Header

    def is_deliveries_items_block_present(self):
        with allure.step("Проверка наличия блока с доставками и товарами в корзине"):
            self.wait_for_selector(self.cart_locators.DELIVERIES_ITEMS_BLOCK)

    def choose_courier_minsk_delivery(self):
        with allure.step(f"Выбор способа доставки - курьер по Минску"):
            self.click(self.cart_locators.RADIO_BTN_COURIER_MINSK)

    def fill_street_field_minsk(self, text):
        with allure.step(f"Заполнение поля 'Улица' значением '{text}' для доставки курьером по Минску"):
            self.input_text(self.cart_locators.MINSK_STREET_INPUT,
                            'Васнецова')  # иногда падает здесь, потому что не появляется список улиц
            self.click(self.cart_locators.MINSK_STREET_LABEL)
            self.click(self.cart_locators.MINSK_STREET_INPUT)
            self.click(self.cart_locators.MINSK_STREET_MAP)

    def fill_house_field_minsk(self, text):
        with allure.step(f"Заполнение поля 'Дом' значением '{text}' для доставки курьером по Минску"):
            self.click(self.cart_locators.MINSK_HOUSE_INPUT)
            self.input_text(self.cart_locators.MINSK_HOUSE_INPUT, text)

    def select_date_of_delivery(self):
        with allure.step("Выбор даты = послезавтра в поле 'Дата доставки'"):
            self.click(self.cart_locators.MINSK_DATE_FIELD)
            unix_date, str_date = get_day_after_tomorrow()
            day_selector = f'a[data-date="{unix_date}"]'
            with allure.step(f"Выбор дня селектором '{day_selector}'"):
                self.wait_for_selector(day_selector)
                self.click(day_selector)
            self.assert_element_has_value(self.cart_locators.MINSK_DATE_FIELD, f'{str_date}')

    def fill_comment_field(self, comment):
        with allure.step(f"Заполнение поля 'Комментарий' текстом '{comment}'"):
            self.input_text(self.cart_locators.COMMENT_FIELD, comment)
            self.assert_element_has_value(self.cart_locators.CHECK_COMMENT, comment)

    def open_auth_popup_in_cart(self):
        with allure.step("Открытие поп-апа авторизации в корзине"):
            self.click(self.cart_locators.CART_AUTH_BTN)

    def go_to_checkout(self):
        with allure.step("Переход к оформлению заказа"):
            self.click(self.cart_locators.TO_CHECKOUT_BTN)

    def assert_no_invalid_field_input(self):
        with allure.step("Проверка на отсутствие невалидно заполненных полей на странице"):
            self.assert_element_hidden(self.cart_locators.NOT_VALID_FIELD_INPUT)

    def place_order_from_cart(self):
        with allure.step("Создание заказа через корзину кнопкой 'Подтвердить и оформить'"):
            self.click(self.cart_locators.TO_PLACE_ORDER_BTN)

    def order_successfully_created(self):
        with allure.step("Проверка вывода поп-апа успешно созданного заказа через корзину"):
            self.is_element_visible(self.cart_locators.ORDER_CREATED_SUCCESSFULLY_POPUP)
            self.is_element_visible(self.cart_locators.ORDER_INFO_BLOCK_IN_SUCCESSFUL_POPUP)

    def close_successful_popup(self):
        with allure.step("Закрытие поп-апа успешно созданного заказа в корзине"):
            self.click(self.cart_locators.CLOSE_SUCCESSFUL_POPUP_BTN)

    def assert_order_history_is_opened_after_order_in_cart(self):
        with allure.step("Проверка открытия страницы 'Мои заказы' после оформления заказа через корзину "
                         "авторизованным пользователем"):
            self.check_url('https://markformelle.by/personal/order/')

    def choose_pickup_delivery(self):
        with allure.step(f"Выбор способа доставки - самовывоз из магазина"):
            self.click(self.cart_locators.RADIO_BTN_PICKUP_CART)

    def assert_store_is_chosen(self):
        with allure.step("Проверка, выбран ли магазин для самовывоза"):
            self.assert_element_hidden(self.cart_locators.NOT_VALID_FIELD_INPUT)
