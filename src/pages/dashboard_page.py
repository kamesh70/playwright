import time
from src.locators import DashboardPageLocators, AddNewUserLocators


class DashBoardPage:

    def __init__(self,page):
        self.page =page
        self.dashboard_header = page.locator(DashboardPageLocators.dashboard_header)
        self.dashboard_user_name = page.locator(DashboardPageLocators.dashboard_user_name)
        self.search_locator = page.get_by_placeholder(DashboardPageLocators.search_locator)
        self.search_item = page.locator(DashboardPageLocators.search_item)
        self.search_headers = page.locator(DashboardPageLocators.search_headers)
        self.add_new_user = page.locator(DashboardPageLocators.add_new_user)
        self.user_role = page.locator(DashboardPageLocators.user_role).nth(0)
        self.status = page.locator(DashboardPageLocators.status).nth(1)
        self.select_admin_option = page.locator(DashboardPageLocators.select_admin_option)
        self.select_enable_option = page.locator(DashboardPageLocators.select_enable_option)
        self.emp_name= page.get_by_placeholder(DashboardPageLocators.emp_name)

        self.username = page.locator(DashboardPageLocators.username).nth(1)
        self.password_input = page.locator(DashboardPageLocators.password_input).nth(0)
        self.confirm_password = page.locator(DashboardPageLocators.confirm_password).nth(1)
        self.save =page.get_by_role(DashboardPageLocators.save_button_role, name=DashboardPageLocators.save_button_name)

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

    def employee_name(self,value):
        self.page.get_by_placeholder(AddNewUserLocators.Username_input).fill(value)
        self.page.wait_for_selector(AddNewUserLocators.wait_input_name)
        self.page.locator(AddNewUserLocators.select_Name).click()


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







