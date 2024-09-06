# test_search.py
import time

from src.pages.login_page import LoginPage
from src.pages.dashboard_page import  DashBoardPage
from tests.configtest import set_up_tear_down, logged_in_page


#/********************************
#Test Scenario 3:Add to new user
#/********************************
def test_add_new_user(logged_in_page) -> None:
    page = logged_in_page
    # login_page = LoginPage(page)  # create LoginPage object
    # credentials = {'username': 'Admin', 'password': 'admin123'}
    # login_page.login(credentials)
    # page.wait_for_load_state('networkidle')
    dashboard_page = DashBoardPage(page)
    dashboard_page.search_click("Admin")
    dashboard_page.new_user()
    dashboard_page.user_role_status()
    data = {'username': 'playwright', 'password': 'Qwerty@123', 'confirm': 'Qwerty@123'}
    dashboard_page.user_name_password_confirm(data)
    dashboard_page.employee_name("Name")
    dashboard_page.save_button()

#/******************************************************
#Test Scenario 2: User Management Search
#/******************************************************
def test_search_keyword(logged_in_page)-> None:
    page = logged_in_page
    time.sleep(3)
    page.get_by_placeholder("Search").fill("Admin")
    time.sleep(1)
    ul_element = page.query_selector('ul.oxd-main-menu')
    if ul_element:
        child_elements = ul_element.query_selector_all('*')
        child_ele = len(child_elements) > 0
        print('Has children:', child_ele)
        if child_ele:
            print('Has children:', child_ele)
            page.locator("//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']").click()

    else:
        page.screenshot(path="element_screenshot.png")
        print('Element not found')







