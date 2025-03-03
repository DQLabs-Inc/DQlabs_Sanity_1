import time
from _ast import And

from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from utils.credential_loader import load_credentials


# @given(u'launching chrome browser')
# def launch_browser(context):
#     pass
#
#
# @when(u'Open DQ home page')
# def dq_homepage(context):
#     context.driver.get(context.base_url)
#     time.sleep(5)
#
#
# @then("enter username and password and enter")
# def enter_credentials(context):
#     credentials = load_credentials("configs/source_connection.json")["login"]
#     username = credentials["username"]
#     password = credentials["password"]
#
#     context.dq_Home.login(username, password)  # Using credentials from JSON
#     time.sleep(2)
#
#
# @then(u'Navigate to discover->Assets')
# def discover_assets(context):
#     context.dq_Home.navigate_to_asset()
#
#
# @when(u'click on the search icon')
# def step_impl(context):
#     context.dq_Home.click_on_search_icon()
#
#
# @when(u'search the asset and connection type')
# def step_impl(context):
#     asset_text = context.credentials["asset"]["name"]
#     context.dq_Home.search_the_asset(asset_text)
#     # context.driver.find_element(By.XPATH, "(//input[@placeholder='Search'])[2]").send_keys("mssql")
#
#
# @then(u'click on the Asset')
# def click_on_the_asset(context):
#     context.dq_Home.click_on_the_asset()


@when(u'click on the More icon')
def click_moreicon(context):
    context.dq_Home.click_on_the_moreicon()


@then(u'click on the schedule button')
def schedule_button(context):
    context.dq_Home.schedule_asset()


@then(u'Enter the Name')
def Enter_the_name(context):
    credentials = load_credentials("configs/source_connection.json")["schedule"]
    name = credentials.get("name")
    context.dq_Home.enter_name(name)


@then(u'select the Repeat frequency')
def step_impl(context):
    context.dq_Home.repeat_frequency("30")


@then(u'click on submit')
def click_on_submit(context):
    context.dq_Home.click_submit()
