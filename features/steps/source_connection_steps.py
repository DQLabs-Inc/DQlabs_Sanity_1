import time
from behave import *
from selenium import webdriver
#from pages.dqlogin_page import LoginPage
from pages.source_connection_page import SourceConnectionPage
from utils.credential_loader import load_credentials

# @given("launch chrome browser")
# def launch_chrome(context):
#     context.driver = webdriver.Chrome()
#     context.driver.maximize_window()
#     context.source_page = SourceConnectionPage(context.driver)

@when("Open DQ labs home page")
def open_home_page(context):
    context.driver.get(context.base_url)

@then("login using credentials from JSON")
def login_using_json(context):
    credentials = load_credentials("configs/source_connection.json")["login"]
    username = credentials["username"]
    password = credentials["password"]

    # ✅ Ensure login_page is initialized once
    #context.login_page = LoginPage(context.driver)
    context.source_page.login(username, password)  # Using credentials from JSON
    time.sleep(5)

# @then("add a new source connection")
# def add_source_connection(context):
#     context.source_page.add_new_connection()
#     context.source_page.enter_connection_details()

@then("click on the profile icon")
def step_click_profile(context):
    context.source_page.click_profile_icon()  # Clicks profile icon
    time.sleep(5)  # Reduce sleep time

@then("navigate to settings")
def step_goto_settings(context):
    context.source_page.click_settings_icon()  # Clicks settings icon
    time.sleep(2)

@then("open options icon")
def open_options_icon(context):
    context.source_page.open_options_icon()
    time.sleep(2)

@then("connect drop down")
def connect_drop_down(context):
    context.source_page.connect_drop_down()
    time.sleep(2)

@then("select source option")
def select_source_option(context):
    context.source_page.select_source_option()
    time.sleep(2)

@then("click on the add new connections")
def step_new_connection(context):
    context.source_page.add_new_connection()

@then('click on the search icon')
def step_click_search_icon(context):
    context.source_page.search_icon()

@then('enter "{text}" in the search field')
def step_enter_search_text(context, text):
    context.source_page.enter_search_text(text)
    time.sleep(5)

@then("select the mssql source")
def step_select_mssql(context):
    context.source_page.select_mssql()

@then("enter connection name")
def step_enter_connection(context):
    context.connection_data = load_credentials("configs/source_connection.json")["source_connection"]
    context.source_page.enter_connection_details(
        context.connection_data["connection_name"],
        context.connection_data["server"],
        context.connection_data["database"],
        context.connection_data["username"],
        context.connection_data["port"],
        context.connection_data["password"],
        context.connection_data["schema"]
    )

@then("click on the validate option")
def step_click_validate(context):
    context.source_page.click_element(*context.source_page.VALIDATE_BUTTON)

@then("enter schema name")
def step_enter_schema(context):
    context.source_page.enter_text(*context.source_page.SCHEMA_NAME, context.connection_data["schema"])

@then("click on the connect option")
def step_click_connect(context):
    context.source_page.connect()
    time.sleep(20)

@then('click on the search button')
def step_click_search_button(context):
    context.source_page.search_button()

@then('enter "{text}" in the search name')
def step_enter_search_text(context, text):
    context.source_page.search_name(text)
    time.sleep(5)

@then("select table check")
def step_impl(context):
    context.source_page.check_box()
    time.sleep(15)

@then("click on connect button")
def step_impl(context):
    context.source_page.click_connect()
    time.sleep(15)

@then("close the browser")
def close_browser(context):
    context.driver.quit()

