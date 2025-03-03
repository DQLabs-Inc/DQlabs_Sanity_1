import time

from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class Pageclass(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

        self.LOGIN_EMAIL = (By.ID, "form_text_email")
        self.LOGIN_PASSWORD = (By.ID, "form_txt_password")
        self.LOGIN_BUTTON = (By.XPATH, "//span[text()='Login']")
        self.DISCOVER_MENU = (By.XPATH, "//span[contains(text(),'Discover')]")
        self.LIST_VIEW = (By.CLASS_NAME, "ListView")
        self.ASSET_TAB = (By.XPATH,
                          "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/form/div/div[1]/div/div[2]/div/div/div/button[8]")
        self.SEARCH_ICON = (
            By.XPATH, "//div[contains(text(),'All')]/../../../../following-sibling::button[1][@aria-label='Search']")

        self.SEARCH_INPUT = (By.XPATH, "(//input[@aria-label='Search'])[1]")
        self.ASSET_ITEM = (By.XPATH, "(//div[@aria-label='Customer'])[1]")

        self.SIDE_BAR_ICON = (By.XPATH, "//body/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/button")
        self.ADD_IDENTIFIER_ICON = (By.XPATH, "//p[contains(text(),'Add Identifier')]")
        self.IDENTIFIER_LIST = (
            By.XPATH, "//input[@placeholder='Select Identifier']/../../../../following-sibling::div/div/ul/li/p[2]")
        self.IDENTIFIER_ELEMENT = (By.XPATH, "//ul/li/p[2][contains(text(),'ID')]")
        self.ADD_DOMAIN_ICON = (By.XPATH, "//p[text()='Add Domain']")
        self.DOMAIN_LIST = (
            By.XPATH, "//input[@placeholder='Select Domain']/../../../../following-sibling::div/div/ul/li/p")
        self.DOMAIN_ELEMENT = (By.XPATH, "//ul/li/p[contains(text(),'Customer')]")
        self.BODY_ELEMENT = (By.XPATH, "//body")
        self.PRODUCT_TAB = (By.XPATH, "(//div[@aria-label='defaultTab'])[2]/button[contains(text(),'Product')]")
        self.ADD_PRODUCT_ICON = (By.XPATH, "//p[contains(text(),'Add Product')]")
        self.PRODUCT_LIST = (
            By.XPATH, "//input[@placeholder='Select Product']/../../../../following-sibling::div/div/ul/li/p")
        self.PRODUCT_ELEMENT = (By.XPATH, "//ul/li/p[contains(text(),'Dq_product')]")
        self.APPLICATION_TAB = (By.XPATH, "(//div[@aria-label='defaultTab'])[2]/button[contains(text(),'App')]")
        self.ADD_APPLICATION_ICON = (By.XPATH, "//p[contains(text(),'Add Application')]")
        self.APPLICATION_LIST = (
            By.XPATH, "//input[@placeholder='Select Application']/../../../../following-sibling::div/div/ul//li//p")
        self.APPLICATION_ELEMENT = (By.XPATH, "//ul//li//p[contains(text(),'SUT_Testing')]")

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

    def side_bar_click(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((self.SIDE_BAR_ICON))).click()

    def refresh_page(self):
        self.driver.refresh()
        time.sleep(10)

    def click_on_side_bar(self):
        self.side_bar_click(self)

    def click_on_add_identifier(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.element_to_be_clickable(self.ADD_IDENTIFIER_ICON)).click()
        time.sleep(2)

    def add_the_identifier(self):
        wait = WebDriverWait(self.driver, 15)

        attributes = self.driver.find_elements(*self.IDENTIFIER_LIST)

        for attribute in attributes:
            if attribute.text.strip() == "ID":
                identifier_element = wait.until(EC.presence_of_element_located(self.IDENTIFIER_ELEMENT))
                wait.until(EC.element_to_be_clickable(self.IDENTIFIER_ELEMENT))
                identifier_element.click()
                time.sleep(2)
                break

    def click_on_add_domain(self):
        wait = WebDriverWait(self.driver, 20)

        add_domain = wait.until(EC.presence_of_element_located(self.ADD_DOMAIN_ICON))

        body_xpath = self.BODY_ELEMENT
        self.driver.find_element(*body_xpath).click()
        time.sleep(1)
        add_domain.click()
        self.refresh_page()
        time.sleep(5)
        self.side_bar_click()

        add_domain = wait.until(EC.element_to_be_clickable(self.ADD_DOMAIN_ICON))
        add_domain.click()

        # Select Domain
        domains = wait.until(EC.presence_of_all_elements_located(self.DOMAIN_LIST))
        for domain in domains:
            if domain.text.strip() == "Customer":
                wait.until(EC.element_to_be_clickable(self.DOMAIN_ELEMENT)
                           ).click()
                time.sleep(2)
                break

    def click_on_product_tab(self):
        wait = WebDriverWait(self.driver, 10)
        product_btn_xpath = self.PRODUCT_TAB
        body_xpath = self.BODY_ELEMENT
        self.driver.find_element(*body_xpath).click()
        time.sleep(1)
        product_btn = wait.until(EC.visibility_of_element_located((product_btn_xpath)))

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_btn)
        wait.until(EC.element_to_be_clickable((product_btn_xpath))).click()

        product_btn.click()
        time.sleep(5)

        add_product = wait.until(
            EC.element_to_be_clickable(self.ADD_PRODUCT_ICON))
        add_product.click()
        time.sleep(10)

    def add_product(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            product = wait.until(EC.presence_of_all_elements_located(self.PRODUCT_LIST))
        except TimeoutException:
            print("❌ No products found. Skipping product selection.")
            return
        for prod in product:
            if prod.text.strip() == "Dq_product":
                wait.until(
                    EC.element_to_be_clickable(self.PRODUCT_ELEMENT)
                ).click()
                time.sleep(2)
                break

    def application_tab(self):
        wait = WebDriverWait(self.driver, 10)

        body_xpath = self.BODY_ELEMENT
        self.driver.find_element(*body_xpath).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable(self.APPLICATION_TAB)).click()

        for _ in range(3):
            add_domain = wait.until(EC.element_to_be_clickable(self.ADD_APPLICATION_ICON))
            add_domain.click()
            time.sleep(2)
            break

    def add_application(self):
        wait = WebDriverWait(self.driver, 10)
        Application = wait.until(EC.presence_of_all_elements_located(self.APPLICATION_LIST))
        for App in Application:
            if App.text.strip() == "SUT_Testing":
                wait.until(
                    EC.element_to_be_clickable(self.APPLICATION_ELEMENT)
                ).click()
                time.sleep(2)
                break
