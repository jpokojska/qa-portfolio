import uuid


def test_guest_can_book_room(reservation_page, cleanup_bookings):
    # Unique last name lets cleanup find exactly the booking created by this test
    lastname = f"Kowalski{uuid.uuid4().hex[:6]}"
    cleanup_bookings.append(lastname)

    reservation_page.goto()
    reservation_page.open_booking_form()
    reservation_page.fill_booking_form(
        firstname="Jan",
        lastname=lastname,
        email="jan.kowalski@test.com",
        phone="01234567890"
    )
    reservation_page.submit_booking()
    reservation_page.expect_booking_confirmed()


def test_booking_fails_without_required_fields(reservation_page):
    reservation_page.goto()
    reservation_page.open_booking_form()
    reservation_page.submit_booking()
    reservation_page.expect_errors_visible()
