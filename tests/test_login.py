import re
import time

from playwright.sync_api import Page, sync_playwright, expect

from src.pages.login_page import LoginPage
from tests.configtest import set_up_tear_down

#/********************************
# 1. Test Scenario 1: User Login
#/********************************
def test_login_with_valid_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'Admin','password': 'admin123'}
    login_page = LoginPage(page)

    dashboard=login_page.login_board(credentials)
    time.sleep(3)
    assert dashboard.dashboard_header.is_visible()
    expect(dashboard.dashboard_header).to_have_text('Dashboard')
    user_name = dashboard.dashboard_user_name
    user_text= user_name.text_content()
    print(f"Logged in user: {user_text}")
    expect(dashboard.dashboard_user_name).to_contain_text(user_text)




def test_login_with_invalid_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    login_page = LoginPage(page)  #  create LoginPage object
    login_page.enter_password('123')
    login_page.enter_username('4323423')
    login_page.click_login()
    error_msg = page.locator("//div[@class='oxd-alert-content oxd-alert-content--error']/p")
    error_text ="Invalid credentials"
    expect(error_msg).to_have_text(error_text)



