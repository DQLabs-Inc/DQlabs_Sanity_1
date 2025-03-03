import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import StaleElementReferenceException

from pages.base_page import BasePage


class Measure(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    LOGIN_EMAIL = (By.ID, "form_text_email")
    LOGIN_PASSWORD = (By.ID, "form_txt_password")
    LOGIN_BUTTON = (By.XPATH, "(//span[contains(text(),'Login')])[1]")
    SETTINGS_ICON = (By.XPATH, "//div[@aria-label='Admin User']")
    SETTINGS_BUTTON = (By.XPATH, "//li[text()='Settings']")
    CONNECT_ICON = (
        By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/h5 ")
    LIBRARIES_ICON = (By.XPATH, "//span[@aria-label='Libraries']")
    PLUS_ICON = (By.XPATH, "(//*[@class='PlusIcon'])[1]")
    LIBRARY_NAME_FIELD = (By.XPATH, "(//input[@placeholder='Enter the name'])[1]")
    DROPDOWN_ELEMENT = (By.XPATH,
                        "//*[@id='private']/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/form/div/div[2]/div/div/div/div[1]/table/thead/tr[2]/th[2]/div/div/div/div/div/div/p")
    LIBRARY_TYPE = (By.XPATH, "//ul/li/p[text()='TABLE']")
    CONFIGURATION_BUTTON = (By.XPATH, "//th/div/div/button[contains(text(),'Configuration')]")
    ADD_CONNECTION_ELEMENT = (By.XPATH, "//*[@id='simple-popover']/div[3]/div/form/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td[1]/div/div/div/div[1]/div/div/button")
    ADD_TABLE = (By.XPATH,
                 "//*[@id='simple-popover']/div[3]/div/form/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td[2]/div/div/div/div[1]/div/div/button")
    ADD_ATTRIBUTES = (By.XPATH,
                      "//*[@id='simple-popover']/div[3]/div/form/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div/button")
    SAVE_BUTTON_ELEMENT = (By.XPATH, "//button[text()='Save']")
    ACTIVE_TOGGLE = (By.XPATH,
                     "//*[@id='private']/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/form/div/div[2]/div/div/div/div[1]/table/thead/tr[2]/th[6]/div/div/div/div/label/span/span[1]/input")
    SAVE_ICON = (By.XPATH, "//*[@id='private']/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/form/div/div[2]/div/div/div/div[1]/table/thead/tr[2]/th[10]/div/div[1]/button")
    CONNECTIONS_LIST = (By.XPATH, "//input[@placeholder='Enter text']/../../../../following-sibling::div/div/ul/li/p")
    CONNECTION_ELEMENT = (By.XPATH, "//ul/li/p[text()='check2_12345i']")
    ASSET_LIST = (By.XPATH, "//input[@placeholder='Enter text']/../../../../following-sibling::div/div/ul/li/p")
    ASSET_ELEMENT = (By.XPATH, "//p[text()='Customer']")
    ATTRIBUTE_LIST = (
        By.XPATH, "//input[@placeholder='Select Attributes']/../../../../following-sibling::div/div/ul/li/p")
    ATTRIBUTE_NAME = (By.XPATH, "//ul/li/p[contains(text(),'ID')]")
    LIBRARY_KEY_ICON = (By.XPATH,"//*[@id='private']/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/form/div/div[2]/div/div/div/div[1]/table/thead/tr[2]/th[8]/div/div/div/div[1]/div/div/button")
    LIBRARY_VALUE = (By.XPATH,"//input[@placeholder='Select Library Key']/../../../../following-sibling::div/div/ul/li/p[contains(text(),'ID')]")

    DISCOVER_MENU = (By.XPATH, "//span[contains(text(),'Discover')]")
    LIST_VIEW = (By.CLASS_NAME, "ListView")
    ASSET_TAB = (By.XPATH,
                 "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/form/div/div[1]/div/div[2]/div/div/div/button[8]")
    SEARCH_ICON = (
        By.XPATH, "//div[contains(text(),'All')]/../../../../following-sibling::button[1][@aria-label='Search']")
    SEARCH_INPUT = (By.XPATH, "(//input[@aria-label='Search'])[1]")
    ASSET_ITEM = (By.XPATH, "(//div[@aria-label='Customer'])[1]")
    ADD_ICON = (By.XPATH, "(//*[@class='PlusIcon'])[1]")
    LOOKUP_TAB = (By.XPATH, "//div[text()='Lookup']")
    NAME_FIELD = (By.XPATH, "//input[@name='name']")
    LOOKUP_TYPE_ELEMENT = (By.XPATH, "//input[@id='lookup_id']")
    ADD_PARAMETER_ELEMENT = (By.XPATH, "(//p[text()='Add parameter'])[1]")
    ADD_PARAMETER_ELEMENT2 = (By.XPATH, "(//p[text()='Add parameter'])[2]")
    ATTRIBUTES_LIST = (By.XPATH, "//input[@placeholder='Enter text']/../../../../following-sibling::div/div/ul/li/p")
    ATTRIBUTE_ELEMENT = (By.XPATH, "//p[contains(text(),'ID')]")
    BODY_ELEMENT = (By.XPATH, "//body")
    SAVE_BUTTON = (By.XPATH, "//span[@class='btnLabel']")

    def login(self, email, password):
        wait = WebDriverWait(self.driver, 10)


        wait.until(EC.element_to_be_clickable(self.LOGIN_EMAIL)).send_keys(email)


        wait.until(EC.element_to_be_clickable(self.LOGIN_PASSWORD)).send_keys(password)



    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        time.sleep(10)

    def navigate_to_libraries(self):
        self.wait.until(EC.presence_of_element_located(self.SETTINGS_ICON))
        self.wait.until(EC.element_to_be_clickable(self.SETTINGS_ICON)).click()

        self.wait.until(EC.presence_of_element_located(self.SETTINGS_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.SETTINGS_BUTTON)).click()

        self.wait.until(EC.presence_of_element_located(self.CONNECT_ICON))
        self.wait.until(EC.element_to_be_clickable(self.CONNECT_ICON)).click()

        self.wait.until(EC.presence_of_element_located(self.LIBRARIES_ICON))
        self.wait.until(EC.element_to_be_clickable(self.LIBRARIES_ICON)).click()

    def create_new_library(self):
        self.wait.until(EC.element_to_be_clickable(self.PLUS_ICON)).click()
        time.sleep(1)

        library_name_field = self.wait.until(EC.element_to_be_clickable(self.LIBRARY_NAME_FIELD))
        library_name_field.clear()
        library_name_field.send_keys("demo2")
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_ELEMENT)).click()
        self.wait.until(EC.element_to_be_clickable(self.LIBRARY_TYPE)).click()


        self.wait.until(EC.element_to_be_clickable(self.CONFIGURATION_BUTTON)).click()
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable(self.ADD_CONNECTION_ELEMENT)).click()
        time.sleep(15)
        self.wait.until(lambda d: len(d.find_elements(*self.CONNECTIONS_LIST)) > 0)

        max_attempts = 10
        attempts = 0

        while attempts < max_attempts:
            connections = self.wait.until(EC.presence_of_all_elements_located(self.CONNECTIONS_LIST))

            for connection in connections:
                if connection.text.strip() == "check2_12345i":
                    self.wait.until(EC.element_to_be_clickable(connection)).click()
                    return

            attempts += 1
            time.sleep(1)


    def add_asset(self):
        body_xpath = self.BODY_ELEMENT
        self.driver.find_element(*body_xpath).click()
        time.sleep(1)


        self.wait.until(EC.element_to_be_clickable(self.ADD_TABLE)).click()
        time.sleep(5)


        assets = self.wait.until(EC.presence_of_all_elements_located(self.ASSET_LIST))
        for asset in assets:
            if asset.text.strip() == "Customer":
                asset_element = self.wait.until(EC.visibility_of_element_located(self.ASSET_ELEMENT))
                try:
                    self.driver.execute_script("arguments[0].click();", asset_element)
                except Exception as e:
                    print(f"JavaScript click failed: {e}, trying normal click.")
                    asset_element.click()
                break
        time.sleep(2)

    def add_attribute(self):
        body_xpath = self.BODY_ELEMENT
        self.driver.find_element(*body_xpath).click()
        time.sleep(1)

        # Add Attributes
        self.wait.until(EC.element_to_be_clickable(self.ADD_ATTRIBUTES)).click()
        time.sleep(5)

        # Select Attribute
        attributes = self.driver.find_elements(*self.ATTRIBUTE_LIST)
        for attribute in attributes:
            if attribute.text.strip() == "ID":
                self.wait.until(EC.element_to_be_clickable(self.ATTRIBUTE_NAME)).click()
                return

    def save_button(self):
        body_xpath = self.BODY_ELEMENT
        self.driver.find_element(*body_xpath).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON_ELEMENT)).click()
        time.sleep(1)

    def active_the_toggle(self):
        body_xpath = self.BODY_ELEMENT
        self.driver.find_element(*body_xpath).click()
        time.sleep(1)

        toggle = self.wait.until(EC.presence_of_element_located(self.ACTIVE_TOGGLE))
        if not toggle.is_selected():
            self.driver.execute_script("arguments[0].click();", toggle)
            time.sleep(5)

    def add_library_key(self):
        body_xpath = self.BODY_ELEMENT
        self.driver.find_element(*body_xpath).click()
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable(self.LIBRARY_KEY_ICON)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.LIBRARY_VALUE)).click()
        time.sleep(1)

    def save_the_library(self):
        body_xpath = self.BODY_ELEMENT
        self.driver.find_element(*body_xpath).click()
        time.sleep(1)
        save_icon = self.wait.until(EC.presence_of_element_located(self.SAVE_ICON))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", save_icon)
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable(self.SAVE_ICON)).click()
        time.sleep(2)


    def navigate_to_asset(self):
      self.wait.until(EC.element_to_be_clickable(self.DISCOVER_MENU)).click()
      time.sleep(1)
      self.wait.until(EC.element_to_be_clickable(self.LIST_VIEW)).click()
      time.sleep(1)
      self.wait.until(EC.element_to_be_clickable(self.ASSET_TAB)).click()
      time.sleep(1)


    def click_on_search_icon(self):
       for attempt in range(3):
         try:
            search_icon = self.wait.until(EC.element_to_be_clickable(self.SEARCH_ICON))
            search_icon.click()
            time.sleep(1)
            break
         except StaleElementReferenceException:
            print(f"Attempt {attempt + 1}: Element went stale, retrying...")
            time.sleep(2)


    def search_the_asset(self, search_text):
      self.driver.find_element(*self.SEARCH_INPUT).send_keys(search_text)
      time.sleep(5)


    def click_on_the_asset(self):
       for attempt in range(3):
         asset_element = self.wait.until(EC.visibility_of_element_located(self.ASSET_ITEM))
         time.sleep(1)

         self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", asset_element)

         self.wait.until(
            EC.element_to_be_clickable(self.ASSET_ITEM))

         asset_element.click()
         break


    def click_on_plus_icon(self):
       attempts = 3

       for attempt in range(attempts):
         try:
            add_icon = self.wait.until(EC.element_to_be_clickable(self.ADD_ICON))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_icon)
            add_icon.click()
            return

         except StaleElementReferenceException:
            print(f"⚠ Attempt {attempt + 1}: Stale element reference! Retrying...")
            time.sleep(2)
            continue


    def navigate_to_lookup_tab(self):
      tab = self.wait.until(EC.element_to_be_clickable(self.LOOKUP_TAB))
      tab.click()


    def name_field(self):
      name_element = self.driver.find_element(*self.NAME_FIELD)
      name_element.send_keys("Lookup")


    def click_on_dropdown(self):
       select_library = self.wait.until(EC.element_to_be_clickable(self.LOOKUP_TYPE_ELEMENT))
       select_library.click()
       select_library.send_keys("demo")
       time.sleep(5)
       select_library.send_keys(Keys.ARROW_DOWN)
       select_library.send_keys(Keys.ENTER)
       time.sleep(1)

    def click_on_add_parameter(self):

        self.driver.find_element(*self.ADD_PARAMETER_ELEMENT).click()
        time.sleep(20)

    def select_lookup_value(self):
       # body_xpath = self.BODY_ELEMENT
       # self.driver.find_element(*body_xpath).click()
       # time.sleep(1)

       self.wait.until(EC.presence_of_all_elements_located(self.ATTRIBUTES_LIST))

       attributes = self.wait.until(EC.visibility_of_all_elements_located(self.ATTRIBUTES_LIST))
       for attribute in attributes:
            if attribute.text.strip() == "ID":
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", attribute)
                self.driver.execute_script("arguments[0].click();", attribute)

                # self.wait.until(EC.element_to_be_clickable(self.ATTRIBUTE_ELEMENT)).click()
                time.sleep(2)
                return

    time.sleep(2)

        # body_xpath = self.BODY_ELEMENT
        # self.driver.find_element(*body_xpath).click()
        # time.sleep(1)
        #
        # self.driver.find_element(*self.ADD_PARAMETER_ELEMENT2).click()
        # time.sleep(1)
        # select_attribute()

    def click_on_save_button(self):
        body_xpath = self.BODY_ELEMENT
        self.driver.find_element(*body_xpath).click()
        time.sleep(1)
        save_button = self.driver.find_element(*self.SAVE_BUTTON)
        save_button.click()
        time.sleep(10)
