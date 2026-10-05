import pytest
import requests
from config import BOOKING_URL

def test_guest_can_book_room(reservation_page, api_token):
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
    bookings = requests.get(
        f"{BOOKING_URL}/booking/",
        cookies={"token": api_token},
        headers={"Accept": "application/json"}
    ).json()
    latest_id = bookings["bookings"][-1]["bookingid"]
    requests.delete(
        f"{BOOKING_URL}/booking/{latest_id}",
        cookies={"token": api_token}
    )



def test_booking_fails_without_required_fields(reservation_page):
    reservation_page.goto()
    reservation_page.open_booking_form()
    reservation_page.submit_booking()
    reservation_page.expect_errors_visible()