class LoginPageLocators:
    USERNAME_FIELD = "Username"
    Password_FIELD = "Password"
    Login_button_role = 'button'
    Login_button_name = 'Login'
    error_msg = "//div[@class='oxd-alert-content oxd-alert-content--error']/p"


class DashboardPageLocators:
    dashboard_header = "h6:has-text('Dashboard')"
    dashboard_user_name = "//span[@class='oxd-userdropdown-tab']/p"
    search_locator = "Search"
    search_item = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']"
    search_headers = "//span[@class='oxd-topbar-header-breadcrumb']/h6"
    add_new_user = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    user_role = "//div[@class='oxd-select-text oxd-select-text--active']"
    status = "//div[@class='oxd-select-text oxd-select-text--active']"
    select_admin_option = "div[role='listbox'].oxd-select-dropdown div:has-text('Admin')"
    select_enable_option = "div[role='listbox'].oxd-select-dropdown div:has-text('Enabled')"
    emp_name = "Type for hints..."
    username = "input[class='oxd-input oxd-input--active']"
    password_input = "input[type='password']"
    confirm_password = "input[type='password']"
    save_button_role = "button"
    save_button_name = "Save"

class AddNewUserLocators:
    Username_input = "Type for hints..."
    wait_input_name = "div[role='listbox'].oxd-autocomplete-dropdown"
    select_Name = "div[role='listbox'].oxd-autocomplete-dropdown div:has-text('FName Mname LName')"

