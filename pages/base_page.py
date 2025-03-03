from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, by, locator, text):
        element = self.driver.find_element(by, locator)
        element.clear()
        element.send_keys(text)

    def click_element(self, by, locator):
        self.driver.find_element(by, locator).click()

    def is_element_present(self, by, locator):
        """Check if an element is present on the page"""
        try:
            self.driver.find_element(by, locator)
            return True
        except NoSuchElementException:
            return False

    # ✅ Common Login Method
    def login(self, username, password):
        """Reusable Login Method for All Pages"""
        EMAIL_FIELD = (By.NAME, "email")
        PASSWORD_FIELD = (By.NAME, "password")
        LOGIN_BUTTON = (By.ID, ":r3:")

        self.enter_text(*EMAIL_FIELD, username)
        self.enter_text(*PASSWORD_FIELD, password)
        self.click_element(*LOGIN_BUTTON)


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def click_element(self, by, locator):
#         self.wait.until(EC.element_to_be_clickable((by, locator))).click()
#
#     def enter_text(self, by, locator, text):
#         self.wait.until(EC.visibility_of_element_located((by, locator))).clear()
#         self.wait.until(EC.visibility_of_element_located((by, locator))).send_keys(text)
#
#     def navigate(self, url):
#         self.driver.get(url)







