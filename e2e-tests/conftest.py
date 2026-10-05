import pytest
import requests

from config import ADMIN_PASSWORD, ADMIN_USERNAME, AUTH_URL, BOOKING_URL

# Browser, context and tracing come from the pytest-playwright plugin
# (see pytest.ini; run with --headed to watch the browser locally).
@pytest.fixture(scope="function")
def page(page):
    page.set_default_timeout(10000)
    return page

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
        json={"username": ADMIN_USERNAME, "password": ADMIN_PASSWORD}
    )
    return response.cookies.get("token")

@pytest.fixture(scope="function")
def cleanup_bookings(api_token):
    """Collect guest last names; matching bookings are deleted after the test, even if it fails."""
    guest_lastnames = []
    yield guest_lastnames
    if not guest_lastnames:
        return
    bookings = requests.get(
        f"{BOOKING_URL}/booking/",
        cookies={"token": api_token},
        headers={"Accept": "application/json"}
    ).json()["bookings"]
    for booking in bookings:
        if booking["lastname"] in guest_lastnames:
            requests.delete(
                f"{BOOKING_URL}/booking/{booking['bookingid']}",
                cookies={"token": api_token}
            )
