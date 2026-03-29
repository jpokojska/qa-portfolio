from playwright.sync_api import Page, expect


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        # Check Availability sekcja
        self.checkin_input = page.get_by_label("Check In")
        self.checkout_input = page.get_by_label("Check Out")
        self.check_availability_button = page.locator("button.btn-primary.w-100")
        # Sekcja Rooms
        self.book_now_buttons = page.locator("a.btn-primary", has_text="Book now")

    def goto(self):
        self.page.goto("http://localhost:3003")

    def check_availability(self, checkin: str, checkout: str):
        self.checkin_input.fill(checkin)
        self.checkout_input.fill(checkout)
        self.check_availability_button.click()

    def book_first_available_room(self):
        self.book_now_buttons.first().click()

    def expect_rooms_visible(self):
        expect(self.book_now_buttons.first()).to_be_visible()