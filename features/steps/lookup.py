from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time
from utils.credential_loader import load_credentials

from selenium.webdriver.support.ui import WebDriverWait


@given(u'Launch Chrome browser')
def launch_browser(context):
    pass


@when(u'Open the application homepage')
def home_page(context):
    context.driver.get(context.base_url)
    time.sleep(5)


@then(u'Enter valid credentials and log in')
def login(context):
    context.credentials = load_credentials("configs/source_connection.json")["login"]
    username = context.credentials["username"]
    password = context.credentials["password"]

    context.look.login(username, password)  # Using credentials from JSON
    time.sleep(2)


@then(u'Click on login')
def login_button(context):
    context.look.click_login()


@when(u'Navigate to libraries')
def libraries(context):
    context.look.navigate_to_libraries()


@then(u'Create new library')
def new_library(context):
    context.look.create_new_library()
    context.look.add_asset()
    context.look.add_attribute()
    context.look.save_button()
    context.look.active_the_toggle()
    context.look.add_library_key()
    context.look.save_the_library()


@then(u'Navigate to the assets')
def asset_navigation(context):
    context.look.navigate_to_asset()


@when(u'Click on the search')
def click_search(context):
    context.look.click_on_search_icon()


@when(u'Search for a specific asset by name')
def enter_text(context):
    context.credentials = load_credentials("configs/source_connection.json")["asset"]
    asset_text = context.credentials["name"]
    context.look.search_the_asset(asset_text)



@then(u'Click on the selected asset')
def select_asset(context):
    context.look.click_on_the_asset()
    time.sleep(1)


@when(u'Click on add icon')
def click_on_add_icon(context):

    context.look.click_on_plus_icon()
    time.sleep(2)


@then(u'Navigate to Lookup tab')
def lookup_tab(context):
    context.look.navigate_to_lookup_tab()
    time.sleep(1)


@then(u'Enter the measure name')
def enter_name(context):
    context.look.name_field()
    time.sleep(1)


@when(u'Select a lookup type')
def lookup_type(context):
    context.look.click_on_dropdown()
    time.sleep(1)


@when(u'Click on add_icon')
def add_icon(context):
    context.look.click_on_add_parameter()


@then(u'Select lookup value')
def lookup_value(context):
    context.look.select_lookup_value()


@then(u'Click on save button')
def save_button(context):
    context.look.click_on_save_button()