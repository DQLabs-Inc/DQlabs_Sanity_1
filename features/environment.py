from selenium import webdriver
from pages.dqlogin_page import LoginPage
from pages.asset_delete_page import AssetDeletePage
from pages.query_measure_page import QueryMeasure
from pages.source_connection_page import SourceConnectionPage
from pages.conditional_measure_page import ConditionalMeasure
from pages.schedule import DQHomePage
from pages.grouping_all import Pageclass
from pages.lookup import Measure

import json


def load_credentials(filepath="/Users/saivamsi/PycharmProjects/DQlabs_Sanity_QA-main/configs/source_connection.json"):
    with open(filepath, "r") as file:
        return json.load(file)


def before_all(context):
    """Setup before all tests run"""
    context.base_url = "https://alpha.qa.dqlabsai.net/"
    # context.base_url = "https://qa3xenv.dqlabsai.net/"

    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

    # def login(self, username, password):
    #         """Logs in using provided credentials"""
    #     self.enter_text(*self.EMAIL_FIELD, username)
    #     self.enter_text(*self.PASSWORD_FIELD, password)
    #     self.click_element(*self.LOGIN_BUTTON)

    # ✅ Initialize Page Objects
    context.login_page = LoginPage(context.driver)
    context.asset_page = AssetDeletePage(context.driver)
    context.source_page = SourceConnectionPage(context.driver)
    context.query_measure = QueryMeasure(context.driver)
    context.conditional_measure = ConditionalMeasure(context.driver)
    context.dq_Home = DQHomePage(context.driver)
    context.page = Pageclass(context.driver)
    context.look = Measure(context.driver)
    #context.credentials = load_credentials("configs/source_connection.json")


def after_all(context):
    """Teardown after all tests"""
    if hasattr(context, "driver"):
        context.driver.quit()
