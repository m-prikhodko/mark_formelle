import allure
from pages.base_page import BasePage
from pages.locators.cart_locators import CartLocators


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_locators = CartLocators()

    def is_deliveries_items_block_present(self):
        with allure.step("Проверка наличия блока с доставками и товарами в корзине"):
            self.wait_for_selector(self.cart_locators.DELIVERIES_ITEMS_BLOCK)

    def choose_courier_minsk_delivery(self):
        with allure.step(f"Выбор способа доставки - курьер по Минску"):
            self.click_button(self.cart_locators.RADIO_BTN_COURIER_MINSK)

    def fill_street_field_minsk(self, text):
        with allure.step(f"Заполнение поля 'Улица' значением {text} для доставки курьером по Минску"):
            self.input_text(self.cart_locators.MINSK_STREET_INPUT, 'Васнецова') # иногда падает здесь, потому что не появляется список улиц
            self.click_button(self.cart_locators.MINSK_STREET_MAP)
