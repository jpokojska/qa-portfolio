import pytest


def test_admin_can_login(admin_login_page):
    admin_login_page.goto()
    admin_login_page.login("admin", "password")
    admin_login_page.expect_logged_in()


def test_admin_login_fails_with_wrong_password(admin_login_page):
    admin_login_page.goto()
    admin_login_page.login("admin", "wrongpassword")
    admin_login_page.expect_logged_out()