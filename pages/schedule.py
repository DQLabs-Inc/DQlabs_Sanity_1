from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

from pages.base_page import BasePage


class DQHomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    LOGIN_EMAIL = (By.ID, "form_text_email")
    LOGIN_PASSWORD = (By.ID, "form_txt_password")
    LOGIN_BUTTON = (By.XPATH, "//span[text()='Login']")
    DISCOVER_MENU = (By.XPATH, "//span[contains(text(),'Discover')]")
    LIST_VIEW = (By.CLASS_NAME, "ListView")
    ASSET_TAB = (By.XPATH,
                 "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/form/div/div[1]/div/div[2]/div/div/div/button[8]")
    SEARCH_ICON = (By.XPATH, "//div[contains(text(),'All')]/../../../../following-sibling::button[1][@aria-label='Search']")
    SEARCH_INPUT = (By.XPATH, "(//input[@aria-label='Search'])[1]")
    ASSET_ITEM = (By.XPATH, "(//div[@aria-label='Customer'])[1]")
    MORE_ICON = (By.XPATH, "(//button[@type='button'])[8]")
    SCHEDULE_BUTTON = (By.XPATH, "//li[3][contains(text(),'Schedule')]")
    NEW_SCHEDULE_RADIO = (By.XPATH, "//input[@type='radio' and @value='New Schedule']")
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    REPEAT_INPUT = (By.XPATH, "//input[@type='number']")
    REPEAT_DROPDOWN = (By.XPATH, "//div[@id='mui-component-select-type']")
    DROPDOWN_LIST = (By.XPATH, "//ul/li/p")
    MINUTES_OPTION = (By.XPATH, "//ul/li/p[contains(text(),'Minutes')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Submit')]")

    def login(self, email, password):
        self.driver.find_element(*self.LOGIN_EMAIL).send_keys(email)
        self.driver.find_element(*self.LOGIN_PASSWORD).send_keys(password)
        time.sleep(2)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def navigate_to_asset(self):
        self.wait.until(EC.element_to_be_clickable(self.DISCOVER_MENU)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.LIST_VIEW)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.ASSET_TAB)).click()
        time.sleep(1)

    def click_on_search_icon(self):
        for attempt in range(3):  # Retry up to 3 times
            try:
                search_icon = self.wait.until(EC.element_to_be_clickable(self.SEARCH_ICON))
                search_icon.click()
                time.sleep(1)
                break  # Exit loop if click is successful
            except StaleElementReferenceException:
                print(f"Attempt {attempt + 1}: Element went stale, retrying...")
                time.sleep(2)

    def search_the_asset(self, search_text):

        self.driver.find_element(*self.SEARCH_INPUT).send_keys(search_text)
        time.sleep(5)

    def click_on_the_asset(self):

        for attempt in range(3):
            asset_element = self.wait.until(EC.presence_of_element_located(self.ASSET_ITEM))
            time.sleep(1)

            asset_element = self.wait.until(EC.visibility_of_element_located(self.ASSET_ITEM))
            time.sleep(1)

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", asset_element)

            self.wait.until(
                EC.element_to_be_clickable(self.ASSET_ITEM))

            asset_element.click()
            break

    def click_on_the_moreicon(self):
        more_icon = self.wait.until(EC.element_to_be_clickable(self.MORE_ICON))

        if more_icon.is_displayed():
            more_icon.click()
        else:
            self.driver.execute_script("arguments[0].click();", more_icon)

    def schedule_asset(self):
        self.wait.until(EC.element_to_be_clickable(self.SCHEDULE_BUTTON)).click()
        time.sleep(1)
        radio_button = self.driver.find_element(*self.NEW_SCHEDULE_RADIO)
        if not radio_button.is_selected():
            radio_button.click()
        time.sleep(1)

    def enter_name(self, name):
        name_input = self.driver.find_element(*self.NAME_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", name_input)
        name_input.clear()
        name_input.send_keys(name)
        time.sleep(2)

    def repeat_frequency(self, value="30"):
        input_field = self.driver.find_element(*self.REPEAT_INPUT)
        time.sleep(1)
        input_field.clear()
        input_field.send_keys(Keys.BACKSPACE)
        input_field.send_keys(value)

        self.driver.find_element(*self.REPEAT_DROPDOWN).click()
        for _ in range(3):
            options = self.wait.until(EC.presence_of_all_elements_located(self.DROPDOWN_LIST))
            for option in options:
                if option.text.strip() == "Minutes":
                    self.driver.find_element(*self.MINUTES_OPTION).click()
                    time.sleep(5)
                    return

    def click_submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(5)