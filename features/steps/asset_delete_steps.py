import time
from behave import *
#from pages.dqlogin_page import LoginPage
from utils.credential_loader import load_credentials

@when("Open DQ labs home page for asset delete")
def open_home_page(context):
    context.driver.get(context.base_url)

@then("login using credentials from JSON file for asset deletion")
def login_using_json_for_asset_delete(context):
    credentials = load_credentials("configs/common_login.json")["login"]
    username = credentials["username"]
    password = credentials["password"]

    #context.login_page = LoginPage(context.driver)
    context.asset_page.login(username, password)  # Using credentials from JSON

@then('navigate to assets page')
def click_asset_page(context):
    context.asset_page.asset_page()
    time.sleep(5)

@then('select list view')
def click_list_view(context):
    context.asset_page.list_view()
    time.sleep(5)

@then('click on search icon')
def click_search_icon(context):
    context.asset_page.search_icon()
    time.sleep(5)

@then('enter "{text}" in the search asset')
def enter_search_asset(context, text):
    context.asset_page.search_asset(text)
    time.sleep(5)

@then('select to delete asset')
def select_delete_asset(context):
    context.asset_page.select_asset()
    time.sleep(5)

@then('click more icon')
def click_more_icon(context):
    context.asset_page.more_icon()
    time.sleep(5)

@then('select delete icon')
def select_delete_asset(context):
    context.asset_page.delete_icon()
    time.sleep(5)

@then('confirm delete asset')
def confirm_delete_asset(context):
    context.asset_page.confirm_delete()
    time.sleep(5)


