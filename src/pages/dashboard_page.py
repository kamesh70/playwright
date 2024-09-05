import time

import pytest

class DashBoardPage:

    def __init__(self,page):
        self.page =page
        self.dashboard_header = page.locator("h6:has-text('Dashboard')")
        self.dashboard_user_name = page.locator("//span[@class='oxd-userdropdown-tab']/p")
        self.search_locator = page.get_by_placeholder("Search")
        self.search_item = page.locator("//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")
        self.search_headers = page.locator("//span[@class='oxd-topbar-header-breadcrumb']/h6")
        self.add_new_user = page.locator("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.user_role = page.locator("//div[@class='oxd-select-text oxd-select-text--active']").nth(0)
        self.status = page.locator("//div[@class='oxd-select-text oxd-select-text--active']").nth(1)
        self.select_admin_option = page.locator("div[role='listbox'].oxd-select-dropdown div:has-text('Admin')")
        self.select_enable_option = page.locator("div[role='listbox'].oxd-select-dropdown div:has-text('Enabled')")
        self.emp_name= page.get_by_placeholder("Type for hints...")

        self.username = page.locator("input[class='oxd-input oxd-input--active']").nth(1)
        self.password_input = page.locator("input[type='password']").nth(0)
        self.confirm_password = page.locator("input[type='password']").nth(1)

        self.save =page.get_by_role("button", name="Save")

    def dashboard_header(self):
        return self.dashboard_header


    def dashboard_user_name(self):
        return self.dashboard_user_name

    def save_button(self):
        self.save.click()

    def enter_username(self,u_name):
        self.username.fill(u_name)

    def enter_password(self,pass_w):
        self.password_input.fill(pass_w)

    def enter_confirm_password(self,c_pass):
        self.confirm_password.fill(c_pass)

    def employee_name(self):
        self.page.get_by_placeholder("Type for hints...").fill("Name")
        self.page.wait_for_selector("div[role='listbox'].oxd-autocomplete-dropdown")
        self.page.locator("div[role='listbox'].oxd-autocomplete-dropdown div:has-text('FName Mname LName')").click()


    def user_role_status(self):
        self.user_role.click()
        self.page.wait_for_selector("div[role='listbox'].oxd-select-dropdown")
        self.select_admin_option.click()
        self.status.click()
        self.select_enable_option.click()
        time.sleep(3)


    def user_name_password_confirm(self, credentials: dict):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.enter_confirm_password(credentials['confirm'])
        time.sleep(3)

    def search_click(self, query):
        self.search_locator.fill(query)
        self.search_item.click()
        time.sleep(3)


    def new_user(self):
        self.add_new_user.click()







