import pytest
import requests
from conftest import AUTH_URL, BOOKING_URL

def get_token():
    response = requests.post(
        f"{AUTH_URL}/auth/login",
        json={"username": "admin", "password": "password"}
    )
    return response.cookies.get("token")

def test_guest_can_book_room(reservation_page):
    reservation_page.goto()
    reservation_page.open_booking_form()
    reservation_page.fill_booking_form(
        firstname="Jan",
        lastname="Kowalski",
        email="jan.kowalski@test.com",
        phone="01234567890"
    )
    reservation_page.submit_booking()
    reservation_page.expect_booking_confirmed()

    # cleanup — usuń ostatnią rezerwację
    token = get_token()
    bookings = requests.get(
        f"{BOOKING_URL}/booking/",
        cookies={"token": token},
        headers={"Accept": "application/json"}
    ).json()
    latest_id = bookings["bookings"][-1]["bookingid"]
    requests.delete(
        f"{BOOKING_URL}/booking/{latest_id}",
        cookies={"token": token}
    )



def test_booking_fails_without_required_fields(reservation_page):
    reservation_page.goto()
    reservation_page.open_booking_form()
    reservation_page.submit_booking()
    reservation_page.expect_errors_visible()