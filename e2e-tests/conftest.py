import pytest
import requests
from playwright.sync_api import sync_playwright

BASE_URL = "http://localhost:3003"
BOOKING_URL = "http://localhost:3000"
AUTH_URL = "http://localhost:3004"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    page.set_default_timeout(10000)
    yield page
    page.close()

@pytest.fixture(scope="function")
def admin_login_page(page):
    from pages.admin_login_page import AdminLoginPage
    return AdminLoginPage(page)

@pytest.fixture(scope="function")
def home_page(page):
    from pages.home_page import HomePage
    return HomePage(page)

@pytest.fixture(scope="function")
def reservation_page(page):
    from pages.reservation_page import ReservationPage
    return ReservationPage(page)

@pytest.fixture(scope="function")
def api_token():
    response = requests.post(
        f"{AUTH_URL}/auth/login",
        json={"username": "admin", "password": "password"}
    )
    token = response.cookies.get("token")
    return token

@pytest.fixture(scope="function")
def cleanup_bookings(api_token):
    created_ids = []

    yield created_ids

    for booking_id in created_ids:
        requests.delete(
            f"{API_URL}/booking/{booking_id}",
            cookies={"token": api_token}
        )

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.set_default_timeout(10000)
    yield page
    context.tracing.stop(path="trace.zip")
    page.close()
    context.close()