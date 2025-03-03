from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AssetDeletePage(BasePage):
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
        select_asset = wait.until(EC.presence_of_element_located(self.SELECT_ASSET))
        select_asset.click()

    def more_icon(self):
        wait = WebDriverWait(self.driver, 20)
        more_icon = wait.until(EC.element_to_be_clickable(self.MORE_ICON))
        more_icon.click()

    def delete_icon(self):
        wait = WebDriverWait(self.driver, 20)
        delete_icon = wait.until(EC.element_to_be_clickable(self.DELETE_ICON))
        delete_icon.click()

    def confirm_delete(self):
        wait = WebDriverWait(self.driver, 20)
        confirm_delete = wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETE))
        confirm_delete.click()
