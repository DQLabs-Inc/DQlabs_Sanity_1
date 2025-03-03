from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class SourceConnectionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.PROFILE_ICON = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/button")
        self.SETTINGS_ICON = (By.CLASS_NAME, "SettingsIcon")
        self.OPEN_OPTIONS_ICON = (By.XPATH, "//*[@id='private']/div[1]/div[2]/div[1]/div[1]/div[1]/button")
        self.CONNECT_DROP_DOWN = (By.XPATH, "//*[@id='private']/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div[2]")
        self.SOURCE_MENU = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div/div/li[1]/p")
        self.ADD_CONNECTION_BUTTON = (By.CLASS_NAME, "PlusIcon")
        self.SEARCH_ICON = (By.CLASS_NAME, "SearchIcon")
        self.SEARCH_FIELD = (By.XPATH, "//*[@id='private']/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[1]/input")
        self.MSSQL_OPTION = (By.XPATH, "//*[@id='private']/div[1]/div[2]/div[1]/div/div/div/div/div/div/div")
        self.CONNECTION_NAME = (By.ID, "name")
        self.SERVER_FIELD = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/form/div[1]/div[3]/div/div/div/div/input")
        self.DATABASE_FIELD = (By.ID, "database")
        self.USERNAME_FIELD = (By.ID, "user")
        self.PORT_FIELD = (By.ID, "port")
        self.PASSWORD_FIELD = (By.ID, "password")
        self.VALIDATE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/form/div[2]/div")
        self.SCHEMA_NAME = (By.ID, "schema")
        self.CONNECT_BUTTON = (By.XPATH, "//*[@id='private']/div[1]/div/div/div/div/div/form/div[2]/div")
        self.SEARCH_BUTTON = (By.XPATH, "//*[@id='private']/div[1]/form/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]")
        self.SEARCH_NAME = (By.XPATH, "//*[@id='private']/div[1]/form/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/table/thead/tr[2]/th[2]/div/div/div/div/div/div/div/div[1]/input")
        self.CHECK_BOX = (By.XPATH,"//*[@id='private']/div[1]/form/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[1]/label")
        self.CLICK_CONNECT = (By.XPATH, "/html/body/div/div/div/div[1]/form/div/div/div/div[3]/div/div[2]/button[2]")

    def click_profile_icon(self):
        wait = WebDriverWait(self.driver, 20)
        profile_icon = wait.until(EC.element_to_be_clickable(self.PROFILE_ICON))
        profile_icon.click()

    def click_settings_icon(self):
        wait = WebDriverWait(self.driver, 10)
        settings_icon = wait.until(EC.element_to_be_clickable(self.SETTINGS_ICON))
        settings_icon.click()

    def open_options_icon(self):
        wait = WebDriverWait(self.driver, 10)
        options_icon = wait.until(EC.element_to_be_clickable(self.OPEN_OPTIONS_ICON))
        options_icon.click()

    def connect_drop_down(self):
        wait = WebDriverWait(self.driver, 10)
        connect_drop_down = wait.until(EC.element_to_be_clickable(self.CONNECT_DROP_DOWN))
        connect_drop_down.click()

    def select_source_option(self):
        wait = WebDriverWait(self.driver, 10)
        source_menu = wait.until(EC.element_to_be_clickable(self.SOURCE_MENU))
        source_menu.click()

    def add_new_connection(self):
        self.click_element(*self.ADD_CONNECTION_BUTTON)

    def search_icon(self):
        wait = WebDriverWait(self.driver, 10)
        search_icon = wait.until(EC.element_to_be_clickable(self.SEARCH_ICON))
        search_icon.click()


    def enter_search_text(self, text):
        wait = WebDriverWait(self.driver, 10)
        search_field = wait.until(EC.presence_of_element_located(self.SEARCH_FIELD))
        search_field.click()
        search_field.clear()
        search_field.send_keys(text)

    def select_mssql(self):
        wait = WebDriverWait(self.driver, 10)
        mssql_option = wait.until(EC.element_to_be_clickable(self.MSSQL_OPTION))
        mssql_option.click()

    def enter_connection_details(self, connection_name, server, database, username, port, password, schema):
        self.enter_text(*self.CONNECTION_NAME, connection_name)
        self.enter_text(*self.SERVER_FIELD, server)
        self.enter_text(*self.DATABASE_FIELD, database)
        self.enter_text(*self.USERNAME_FIELD, username)
        self.enter_text(*self.PORT_FIELD, port)
        self.enter_text(*self.PASSWORD_FIELD, password)
        self.click_element(*self.VALIDATE_BUTTON)
        self.enter_text(*self.SCHEMA_NAME, schema)

    def connect(self):
        wait = WebDriverWait(self.driver, 50)

        print(f"🔍 Looking for CONNECT_BUTTON: {self.CONNECT_BUTTON}")

        try:
            # ✅ Wait until the first Connect button is visible and clickable
            connect_button = wait.until(EC.element_to_be_clickable(self.CONNECT_BUTTON))

            # ✅ Scroll into view to avoid interception
            self.driver.execute_script("arguments[0].scrollIntoView();", connect_button)

            # ✅ Click the button
            connect_button.click()
            print("✅ First Connect button clicked!")

            # ✅ Stop Selenium from looking for another Connect button
            # Wait for the button to disappear after clicking (staleness check)
            wait.until(EC.staleness_of(connect_button))
            print("✅ First Connect button removed!")

            # ✅ Ensure the new page loads completely before any further steps
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
            print("✅ New page loaded successfully!")

        except TimeoutException:
            print("⏳ ERROR: Timeout while waiting for CONNECT_BUTTON!")
            raise

    def search_button(self):
        wait = WebDriverWait(self.driver, 10)
        search_button = wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search_button.click()

    def search_name(self, text):
        wait = WebDriverWait(self.driver, 10)
        search_name = wait.until(EC.presence_of_element_located(self.SEARCH_NAME))
        search_name.click()
        search_name.clear()
        search_name.send_keys(text)

    def check_box(self):
        wait = WebDriverWait(self.driver, 10)
        check_box = wait.until(EC.element_to_be_clickable(self.CHECK_BOX))
        check_box.click()

    def click_connect(self):
        wait = WebDriverWait(self.driver, 30)
        click_connect = wait.until(EC.element_to_be_clickable(self.CLICK_CONNECT))
        click_connect.click()
