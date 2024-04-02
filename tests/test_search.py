from pages.page_elements.header_element import Header
from pages.page_elements.listing_element import Listing
from data.urls import BASE_URL_BY


def test_search(page):
    header = Header(page)
    listing = Listing(page)
    header.navigate(BASE_URL_BY)
    header.send_search_request("платье")
    listing.assert_presence_of_item()
    listing.assert_all_catalog_items_contain_text("платье")
