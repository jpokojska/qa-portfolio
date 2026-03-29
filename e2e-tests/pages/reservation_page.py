from playwright.sync_api import Page, expect
from datetime import datetime, timedelta


class ReservationPage:

    def __init__(self, page: Page):
        self.page = page
        self.reserve_now_button = page.locator("button.btn-primary.w-100")
        self.firstname_input = page.locator(".room-firstname")
        self.lastname_input = page.locator(".room-lastname")
        self.email_input = page.locator(".room-email")
        self.phone_input = page.locator(".room-phone")
        self.cancel_button = page.locator("button.btn-secondary.w-100")
        self.success_message = page.locator(".card-body", has_text="Booking Confirmed")

    def goto(self, room_id: int = 3, nights: int = 2):
        checkin = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
        checkout = (datetime.now() + timedelta(days=7 + nights)).strftime("%Y-%m-%d")
        self.page.goto(f"http://localhost:3003/reservation/{room_id}?checkin={checkin}&checkout={checkout}")

    def open_booking_form(self):
        self.page.wait_for_timeout(500)
        self.reserve_now_button.click()
        
        expect(self.firstname_input).to_be_visible()

    def fill_booking_form(self, firstname: str, lastname: str, email: str, phone: str):
        self.firstname_input.fill(firstname)
        self.lastname_input.fill(lastname)
        self.email_input.fill(email)
        self.phone_input.fill(phone)

    def submit_booking(self):
        self.reserve_now_button.click()

    def cancel_booking(self):
        self.cancel_button.click()

    def expect_booking_confirmed(self):
        expect(self.success_message).to_be_visible()

    def expect_errors_visible(self):
        expect(self.page.locator(".alert.alert-danger")).to_be_visible()