from playwright.sync_api import Page
from pages.cart_page import CartPage
from pages.page_elements.header_element import Header
from pages.page_elements.listing_element import Listing
from data.urls import BASE_URL


def test_courier_minsk(page: Page):
    header = Header(page)
    listing = Listing(page)
    cart = CartPage(page)
    header.navigate(BASE_URL)
    header.open_catalog()
    header.go_to_all_for_women()
    listing.show_available_online_items()
    # listing.open_item_cart_from_listing()
    # listing.close_mindbox_popup()
    listing.add_item_to_cart_from_listing()
    header.open_cart()
    cart.is_deliveries_items_block_present()
    cart.choose_courier_minsk_delivery()
    cart.fill_street_field_minsk('Васнецова')

