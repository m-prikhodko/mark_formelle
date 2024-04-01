import time
from playwright.sync_api import BrowserContext
from playwright.sync_api import Page
from pages.cart_page import CartPage
from pages.page_elements.cookie_popup_element import CookiePopup
from pages.page_elements.header_element import Header
from pages.page_elements.listing_element import Listing
from data.urls import BASE_URL_BY
from pages.profile_page import ProfilePage


def test_courier_minsk_pay_on_delivery(page: Page):
    context: BrowserContext = page.context
    # Начать запись трассировки
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    try:
        header = Header(page)
        listing = Listing(page)
        cart = CartPage(page)
        cookie = CookiePopup(page)
        profile = ProfilePage(page)
        header.navigate(BASE_URL_BY)
        cookie.reject_cookie_by()
        header.open_catalog()
        header.go_to_all_for_women()
        listing.show_available_online_items()
        listing.add_item_to_cart_from_listing()
        header.open_cart()
        cart.is_deliveries_items_block_present()
        cart.open_auth_popup_in_cart()
        header.login_with_login_pwd('375292463073', '123456')
        time.sleep(2)  # нужно, чтобы не попадать на плавающий дефект в корзине
        cart.choose_courier_minsk_delivery()
        cart.fill_street_field_cart('Васнецова')
        cart.fill_house_field_cart('1')
        cart.select_date_of_delivery()
        cart.fill_comment_field('тестовый заказ')
        cart.assert_no_invalid_field_input()
        cart.go_to_checkout()
        cart.assert_no_invalid_field_input()
        cart.place_order_from_cart()
        cart.order_successfully_created()
        cart.close_successful_popup()
        cart.assert_order_history_is_opened_after_order_in_cart()
        profile.cancel_order_from_profile()
    finally:
        context.tracing.stop(path="trace.zip")


def test_pickup_from_cart(page: Page):
    context: BrowserContext = page.context
    # Начать запись трассировки
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    try:
        header = Header(page)
        listing = Listing(page)
        cart = CartPage(page)
        cookie = CookiePopup(page)
        profile = ProfilePage(page)
        header.navigate(BASE_URL_BY)
        cookie.reject_cookie_by()
        header.open_catalog()
        header.go_to_all_for_men()
        listing.show_available_online_items()
        listing.add_item_to_cart_from_listing()
        header.open_cart()
        cart.is_deliveries_items_block_present()
        cart.open_auth_popup_in_cart()
        header.login_with_login_pwd('375292463073', '123456')
        cart.choose_pickup_delivery()
        cart.assert_store_is_chosen()
        cart.go_to_checkout()
        cart.assert_no_invalid_field_input()
        cart.place_order_from_cart()
        cart.order_successfully_created()
        cart.close_successful_popup()
        cart.assert_order_history_is_opened_after_order_in_cart()
        profile.cancel_order_from_profile()
    finally:
        context.tracing.stop(path="trace.zip")


def test_post_pay_by_card(page: Page):
    context: BrowserContext = page.context
    # Начать запись трассировки
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    try:
        header = Header(page)
        listing = Listing(page)
        cart = CartPage(page)
        cookie = CookiePopup(page)
        profile = ProfilePage(page)
        header.navigate(BASE_URL_BY)
        cookie.reject_cookie_by()
        header.change_user_location()
        header.open_catalog()
        header.go_to_all_for_girls()
        listing.show_available_online_items()
        listing.add_item_to_cart_from_listing()
        header.open_cart()
        cart.is_deliveries_items_block_present()
        cart.open_auth_popup_in_cart()
        header.login_with_login_pwd('375292463073', '123456')
        cart.choose_delivery_by_post()
        cart.fill_street_field_cart('Советская')
        cart.fill_house_field_cart('1')
        cart.fill_postcode_field_cart('111111')
        cart.fill_comment_field('тестовый заказ')
        cart.assert_no_invalid_field_input()
        cart.go_to_checkout()
        cart.choose_pay_by_card_in_cart()
        cart.assert_no_invalid_field_input()
        cart.place_order_from_cart()
        cart.order_successfully_created()
        cart.assert_assist_page_is_opened()
        cart.close_successful_popup()
        cart.assert_order_history_is_opened_after_order_in_cart()
        profile.cancel_order_from_profile()
    finally:
        context.tracing.stop(path="trace.zip")
