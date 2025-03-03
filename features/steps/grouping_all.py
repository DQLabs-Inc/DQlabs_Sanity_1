import time
from behave import given, when, then
from utils.credential_loader import load_credentials


@given("launching chrome browser")
def launch_browser(context):
    pass


@when("Open DQ home page")
def dq_homepage(context):
    context.driver.get(context.base_url)
    time.sleep(5)


@then("enter username and password and enter")
def enter_credentials(context):
    context.credentials = load_credentials("configs/source_connection.json")["login"]
    username = context.credentials["username"]
    password = context.credentials["password"]

    context.page.login(username, password)  # Using credentials from JSON
    time.sleep(2)


@then("Navigate to discover->Assets")
def discover_assets(context):
    context.page.navigate_to_asset()


@when("click on the search icon")
def search_icon(context):
    context.page.click_on_search_icon()


@when("search the asset and connection type")
def search_the_asset(context):
    context.credentials = load_credentials("configs/source_connection.json")["asset"]
    asset_text = context.credentials["name"]
    context.page.search_the_asset(asset_text)
    # context.driver.find_element(By.XPATH, "(//input[@placeholder='Search'])[2]").send_keys("mssql")


@then("click on the Asset")
def click_on_the_asset(context):
    context.page.click_on_the_asset()


@when("open the side bar")
def open_side_bar(context):
    context.page.side_bar_click()


@when("add the identifier")
def add_identifier(context):
    context.page.click_on_add_identifier()
    context.page.add_the_identifier()


@when("add the domain")
def add_domain(context):
    context.page.click_on_add_domain()


@when("add the product")
def add_product(context):
    context.page.click_on_product_tab()
    context.page.add_product()


@when("add the Application")
def add_application(context):
    context.page.application_tab()
    context.page.add_application()
