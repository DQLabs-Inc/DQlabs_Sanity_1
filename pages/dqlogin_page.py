from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # ✅ Define locators correctly
        self.EMAIL_FIELD = (By.NAME, "email")
        self.PASSWORD_FIELD = (By.NAME, "password")
        self.LOGIN_BUTTON = (By.ID, ":r3:")
        self.ERROR_MESSAGE = (By.CLASS_NAME, "error-message")  # Adjust if needed

    def load_login_page(self, url):
        """Opens the login page"""
        self.driver.get(url)

    # def login(self, username, password):
    #     """Logs in using provided credentials"""
    #     self.enter_text(*self.EMAIL_FIELD, username)
    #     self.enter_text(*self.PASSWORD_FIELD, password)
    #     self.click_element(*self.LOGIN_BUTTON)

    def is_login_successful(self):
        """Checks if login was successful"""
        return "dashboard" in self.driver.current_url  # Adjust based on UI

    def is_login_failed(self):
        """Checks if login failed based on UI message"""
        return self.is_element_present(*self.ERROR_MESSAGE)

    def is_element_present(self, by, locator):
        """Check if an element is present on the page"""
        try:
            self.driver.find_element(by, locator)
            return True
        except NoSuchElementException:
            return False


# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from pages.base_page import BasePage
#
# class LoginPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#
#         # ✅ Define locators correctly
#         self.EMAIL_FIELD = (By.NAME, "email")
#         self.PASSWORD_FIELD = (By.NAME, "password")
#         self.LOGIN_BUTTON = (By.ID, ":r3:")
#         self.ERROR_MESSAGE = (By.CLASS_NAME, "error-message")  # Adjust if needed
#
#     def load_login_page(self, url):
#         """Opens the login page"""
#         self.driver.get(url)
#
#     def login(self, username, password):
#         """Logs in using provided credentials"""
#         self.enter_text(*self.EMAIL_FIELD, username)
#         self.enter_text(*self.PASSWORD_FIELD, password)
#         self.click_element(*self.LOGIN_BUTTON)
#
#     def is_login_successful(self):
#         """Checks if login was successful"""
#         return "dashboard" in self.driver.current_url  # Adjust based on UI
#
#     def is_login_failed(self):
#         """Checks if login failed based on UI message"""
#         return self.is_element_present(*self.ERROR_MESSAGE)
#
#     def is_element_present(self, by, locator):
#         """Check if an element is present on the page"""
#         try:
#             self.driver.find_element(by, locator)
#             return True
#         except NoSuchElementException:
#             return False


