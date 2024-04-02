import allure
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(params=["firefox"])
# params=["chromium", "firefox", "webkit"]
def page(request):
    playwright = sync_playwright().start()
    browser = getattr(playwright, request.param).launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.set_viewport_size({"width": 1440, "height": 900})
    yield page
    test_name = request.node.name
    trace_file = f'result/{test_name}_trace.zip'
    context.tracing.stop(path=trace_file)
    browser.close()
    playwright.stop()
    # Добавляем трассировку как вложение в Allure
    with allure.step("Generating trace.zip file"):
        with open(trace_file, 'rb') as f:
            allure.attach(f.read(), name=test_name + "_trace.zip", attachment_type='application/zip')
