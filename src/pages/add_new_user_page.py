


class AddNewUser:

    def __init__(self,page):
        self.page = page
        self.add_new_user= self.page.locator("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")

    def create_new_user(self):
        self.add_new_user.click()
        add_user =self.page.locator("//div[@class='orangehrm-card-container']/h6")
        print(add_user.text_content())