from tkinter.constants import SEL_FIRST

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time

class ConditionalMeasure(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.ASSET_PAGE = (By.XPATH, "//*[@id='root']/div/div[1]/div[1]/div[2]/button[3]")
        self.LIST_VIEW = (By.CLASS_NAME, "ListView")
        self.SEARCH_ICON = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/form/div/div[1]/div/div[2]/button[1]")
        self.SEARCH_ASSET = (By.XPATH, "//*[@id='private']/div[1]/div[2]/div/div/div/div/div/div/div/form/div/div[2]/div/div/div/div[1]/table/thead/tr[2]/th[1]/div/div/div/div/div/div/div/div[1]/input")
        self.SELECT_ASSET = (By.XPATH,"//*[@id='private']/div[1]/div[2]/div/div/div/div/div/div/div/form/div/div[2]/div/div/div/div[1]/table/tbody/tr[1]/td[1]/div/div/div/div/p")
        self.MORE_ICON = (By.CLASS_NAME, "MoreIcon")
        self.DELETE_ICON = (By.CLASS_NAME, "DeleteIcon")
        self.CONFIRM_DELETE = (By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div/div/button[2]")
        self.ADD_MEASURES = (By.XPATH, "//*[@id='private']/div[1]/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/form/div/div[1]/div/div[2]/button[2]")
        #Creating conditional measure
        self.ENTER_ATTRIBUTE = (By.XPATH, "/html/body/div/div/div/form/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/input")
        self.SELECT_ATTRIBUTE = (By.ID,":r1gc:-option-0")
        self.ENTER_CONDITION = (By.XPATH, "/html/body/div/div/div/form/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/div/input")
        self.SELECT_CONDITION = (By.ID, ":r1ge:-option-0")

        # self.CONDITIONAL_ATTRIBUTE_DROP_DOWN = (By.XPATH, "//*[@id='private']/form/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div")
        # self.CONDITION_VALUE = (By.XPATH, "/html/body/div[2]/div/ul")
        #self.CONDITION_VALUE = (By.XPATH, "/html/body/div/div/div/form/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/div/input")



    def asset_page(self):
        wait = WebDriverWait(self.driver, 20)
        asset_page = wait.until(EC.element_to_be_clickable(self.ASSET_PAGE))
        asset_page.click()

    def list_view(self):
        wait = WebDriverWait(self.driver, 20)
        list_view = wait.until(EC.element_to_be_clickable(self.LIST_VIEW))
        list_view.click()

    def search_icon(self):
        wait = WebDriverWait(self.driver, 20)
        search_icon = wait.until(EC.element_to_be_clickable(self.SEARCH_ICON))
        search_icon.click()

    def search_asset(self, text):
        wait = WebDriverWait(self.driver, 20)
        search_asset = wait.until(EC.presence_of_element_located(self.SEARCH_ASSET))
        search_asset.click()
        search_asset.clear()
        search_asset.send_keys(text)

    def select_asset(self):
        wait = WebDriverWait(self.driver, 20)
        select_asset = wait.until(EC.element_to_be_clickable(self.SELECT_ASSET))
        select_asset.click()

    def add_measure(self):
        wait = WebDriverWait(self.driver, 20)
        add_measures = wait.until(EC.element_to_be_clickable(self.ADD_MEASURES))
        add_measures.click()

    def select_conditional_attribute(self, text):
        wait = WebDriverWait(self.driver, 20)
        select_conditional_attribute = wait.until(EC.presence_of_element_located(self.ENTER_ATTRIBUTE))
        select_conditional_attribute.click()
        select_conditional_attribute.clear()
        select_conditional_attribute.send_keys(text)

    def select_condition_value(self, text):
        wait = WebDriverWait(self.driver, 20)
        select_condition_value = wait.until(EC.presence_of_element_located(self.ENTER_CONDITION))
        select_condition_value.click()
        select_condition_value.clear()
        select_condition_value.send_keys(text)

    # Working
    # def select_conditional_attribute(self, text):
    #     wait = WebDriverWait(self.driver, 20)
    #     actions = ActionChains(self.driver)
    #
    #     dropdown = wait.until(EC.element_to_be_clickable(self.CONDITIONAL_ATTRIBUTE_DROP_DOWN))
    #     dropdown.click()
    #     time.sleep(2)  # Allow time for options to load (Adjust if needed)
    #
    #     try:
    #         dropdown_list = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div//li")))
    #         print("Dropdown list is now visible")
    #     except Exception:
    #         print("Dropdown list did not appear! Check the XPath or loading delay.")
    #         return
    #
    #     try:
    #         options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[2]/div//li")))
    #         print("Found dropdown options")
    #     except Exception:
    #         print("Dropdown options not found! Check XPath.")
    #         return
    #
    #     dropdown_values = [option.text for option in options]
    #     print(f"Dropdown values found: {dropdown_values}")
    #
    #     for option in options:
    #         if option.text.strip() == text:  # Match with input parameter
    #             actions.move_to_element(option).click().perform()
    #             print(f" Selected '{text}' from dropdown")
    #             break  # Stop after selection
    #
    #     time.sleep(2)

    # Working
    # def select_condition_value(self, text):
    #     wait = WebDriverWait(self.driver, 20)
    #     actions = ActionChains(self.driver)
    #
    #     dropdown = wait.until(EC.element_to_be_clickable(self.CONDITION_VALUE))
    #     dropdown.click()
    #     print("Clicked dropdown to expand options")
    #     time.sleep(2)  # Allow time for options to load (Adjust if needed)
    #
    #     try:
    #         dropdown_list = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/ul")))
    #         print("Dropdown list is now visible")
    #     except Exception:
    #         print("Dropdown list did not appear! Check the XPath or loading delay.")
    #         return
    #
    #     try:
    #         options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[2]/div/ul")))
    #         print("Found dropdown options")
    #     except Exception:
    #         print("Dropdown options not found! Check XPath.")
    #         return
    #
    #     dropdown_values = [option.text for option in options]
    #     print(f"Dropdown values found: {dropdown_values}")
    #
    #     for option in options:
    #         if option.text.strip() == text:  # Match with input parameter
    #             actions.move_to_element(option).click().perform()
    #             print(f"Selected '{text}' from dropdown")
    #             break  # Stop after selection
    #
    #     time.sleep(2)

