import  pytest

@pytest.fixture()
def set_up_tear_down(page)->None:
    page.set_default_timeout(60000)  # Set to 60 seconds
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield page