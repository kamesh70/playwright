from playwright.sync_api import Page, sync_playwright, expect

from src.pages.dashboard_page import DashBoardPage


class LoginPage:

    def __init__(self,page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role("button", name="Login")


    def enter_username(self,u_name):
        self.username.clear()
        self.username.fill(u_name)

    def enter_password(self,p_word):
        self.password.clear()
        self.password.fill(p_word)

    def click_login(self):
        self.login_btn.click()

    def login_board(self, credentials: dict):
        try:
            # self.page.wait_for_load_state("networkidle")
            self.enter_username(credentials['username'])
            self.enter_password(credentials['password'])
            self.click_login()
            self.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index",timeout=10000)
            return DashBoardPage(self.page)
        except Exception as e:
            self.page.screenshot(path="element_screenshot.png")
            print(f"An error occurred during login: {e}")
            raise  # Optionally re-raise the exception to fail the test


    def login(self,credentials:dict ):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.click_login()