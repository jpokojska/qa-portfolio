import pytest
from playwright.sync_api import sync_playwright, Page

BASE_URL = "http://localhost:3003"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False - zobaczysz przeglądarkę
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    page.set_default_timeout(10000)  # 10 sekund timeout
    yield page
    page.close()

@pytest.fixture(scope="function")
def admin_login_page(page):
    from pages.admin_login_page import AdminLoginPage
    return AdminLoginPage(page)

@pytest.fixture(scope="function")
def booking_page(page):
    from pages.booking_page import BookingPage
    return BookingPage(page)