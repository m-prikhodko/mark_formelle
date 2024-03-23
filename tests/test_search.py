from playwright.sync_api import Page
from pages.page_elements.header_element import Header
from pages.page_elements.listing_element import Listing
from data.urls import BASE_URL


def test_search(page: Page):
    header = Header(page)
    listing = Listing(page)
    header.navigate(BASE_URL)
    header.send_search_request("платье")
    listing.assert_presence_of_item()
