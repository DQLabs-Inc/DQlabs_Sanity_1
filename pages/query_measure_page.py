from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time

class QueryMeasure(BasePage):
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

        # Creating query measure
        self.ENTER_MEASURE_NAME = (By.XPATH,"/html/body/div/div/div/form/div/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div/div/input")
        self.SELECT_QUERY_MEASURE = (By.XPATH, "/html/body/div/div/div/form/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/button[2]/div")
        self.PROVIDE_QUERY = (By.XPATH,"/html/body/div/div/div/form/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div")


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

    def select_query_measure(self):
        wait = WebDriverWait(self.driver, 20)
        select_query = wait.until(EC.element_to_be_clickable(self.SELECT_QUERY_MEASURE))
        select_query.click()

    def enter_measure_name(self, text):
        wait = WebDriverWait(self.driver, 20)
        measure_name = wait.until(EC.presence_of_element_located(self.ENTER_MEASURE_NAME))
        measure_name.click()
        measure_name.clear()
        measure_name.send_keys(text)

    def provide_query(self, text):
        wait = WebDriverWait(self.driver, 20)
        provide_query = wait.until(EC.presence_of_element_located(self.PROVIDE_QUERY))
        provide_query.click()
        provide_query.clear()
        provide_query.send_keys(text)

    # def provide_query(self, text):
    #     wait = WebDriverWait(self.driver, 30)  # Increased wait time
    #
    #     # ✅ Ensure element is present
    #     provide_query = wait.until(EC.presence_of_element_located(self.PROVIDE_QUERY))
    #
    #     # ✅ Check if element is enabled
    #     if not provide_query.is_enabled():
    #         print("❌ Input field is disabled! Cannot enter text.")
    #         return
    #
    #     # ✅ Handle if the field is read-only
    #     if provide_query.get_attribute("readonly"):
    #         print("❌ Input field is read-only! Trying to remove attribute.")
    #         self.driver.execute_script("arguments[0].removeAttribute('readonly');", provide_query)
    #
    #     # ✅ Ensure element is clickable before interacting
    #     wait.until(EC.element_to_be_clickable(self.PROVIDE_QUERY))
    #
    #     # ✅ Remove any overlays if they exist
    #     try:
    #         overlay = self.driver.find_element(By.XPATH, "//div[contains(@class, 'overlay')]")  # Adjust XPath as needed
    #         self.driver.execute_script("arguments[0].style.display='none';", overlay)
    #         print("✅ Overlay removed successfully!")
    #     except Exception:
    #         pass  # No overlay found, continue
    #
    #     # ✅ Scroll into view to avoid hidden element issue
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", provide_query)
    #     time.sleep(1)  # Allow time for adjustments
    #
    #     # ✅ Click, clear, and enter text
    #     provide_query.click()
    #     provide_query.clear()
    #     provide_query.send_keys(text)
    #     print(f"✅ Successfully entered query: {text}")
    #
    #     time.sleep(2)  # Allow time for input to reflect
