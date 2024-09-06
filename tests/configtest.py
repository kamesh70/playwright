import  pytest
from src.pages.login_page import LoginPage



@pytest.fixture()
def set_up_tear_down(page)->None:
    page.set_default_timeout(60000)  # Set to 60 seconds
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield page

@pytest.fixture
def logged_in_page(set_up_tear_down):
    page = set_up_tear_down
    login_page = LoginPage(page)
    credentials = {'username': 'Admin', 'password': 'admin123'}
    login_page.login(credentials)
    page.wait_for_load_state('networkidle')
    return page
