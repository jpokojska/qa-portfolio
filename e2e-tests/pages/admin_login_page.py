from playwright.sync_api import Page, expect


class AdminLoginPage:

    def __init__(self, page: Page):
        self.page = page
        # Selektory
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#doLogin")
        self.logout_button = page.locator("button.btn-outline-danger", has_text="Logout")

    def goto(self):
        self.page.goto("http://localhost:3003/admin")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
        self.logout_button.click()

    def expect_logged_in(self):
        expect(self.page).to_have_url("http://localhost:3003/admin/rooms")
        expect(self.logout_button).to_be_visible()

    def expect_logged_out(self):
        expect(self.page.locator("#username")).to_be_visible()