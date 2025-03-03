import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#from pages.dqlogin_page import LoginPage
from utils.credential_loader import load_credentials
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@given('launch dqlabs home page')
def open_home_page(context):
    context.driver.get(context.base_url)
    time.sleep(5)

@when('login using credentials from JSON for conditional measures creation')
def login_using_json_for_asset_delete(context):
    credentials = load_credentials("configs/common_login.json")["login"]
    username = credentials["username"]
    password = credentials["password"]

    #context.login_page = LoginPage(context.driver)
    context.conditional_measure.login(username, password)  # Using credentials from JSON
    time.sleep(10)

@then('switch to assets main page')
def click_asset_page(context):
    context.conditional_measure.asset_page()
    time.sleep(10)

@then('click list view page')
def click_list_view(context):
    context.conditional_measure.list_view()
    time.sleep(5)

@then('select icon to search')
def click_search_icon(context):
    context.conditional_measure.search_icon()
    time.sleep(5)

@then('enter "{text}" in the search area')
def enter_search_asset(context, text):
    context.conditional_measure.search_asset(text)
    time.sleep(5)

@then('select the asset to add conditional measure')
def select_delete_asset(context):
    context.conditional_measure.select_asset()
    time.sleep(5)

from selenium.common.exceptions import StaleElementReferenceException

@then('click on add button to create conditional measure')
def click_add_button(context):
    try:
        wait = WebDriverWait(context.driver, 20)

        # Wait until the add button is clickable (using an appropriate locator)
        add_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "PlusIcon")))  # Adjust locator if needed

        # Scroll into view before clicking
        context.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", add_button)

        # Wait until the element is visible
        wait.until(EC.visibility_of(add_button))  # Ensures the element is visible before clicking

        # Retry mechanism in case the element becomes stale
        retry_attempts = 3
        for attempt in range(retry_attempts):
            try:
                # Click the button
                add_button.click()
                break  # If click is successful, break out of the loop
            except StaleElementReferenceException:
                if attempt == retry_attempts - 1:
                    print(f"Error: StaleElementReferenceException after {retry_attempts} attempts")
                    raise  # Re-raise exception after max attempts
                print(f"Retrying due to StaleElementReferenceException, attempt {attempt + 1} of {retry_attempts}")
                add_button = wait.until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "PlusIcon")))  # Re-find the button after stale element

        # Wait to give time for the action to be completed
        WebDriverWait(context.driver, 5).until(
            EC.staleness_of(add_button))  # Wait until the button is no longer in the DOM

    except Exception as e:
        print(f"Error: {e}")
        raise  # Re-raise the exception for better debugging and logging


# @then('select attribute value')
# def select_attribute_value(context):
#     wait = WebDriverWait(context.driver, 30)  # Increased timeout
#     actions = ActionChains(context.driver)
#
#     dropdown = wait.until(EC.element_to_be_clickable(context.save_measures_page.CONDITIONAL_ATTRIBUTE_DROP_DOWN))
#     dropdown.click()
#     print("Clicked dropdown")
#
#     try:
#         dropdown_list = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div")))
#         print("Dropdown list is now visible")
#     except Exception:
#         print("Dropdown list did not appear! Check the XPath or wait time.")
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
#     target_value = "FirstName"
#     for option in options:
#         if option.text.strip() == target_value:
#             actions.move_to_element(option).click().perform()
#             print(f"Selected '{target_value}' from dropdown")
#             break  # Exit loop after selection
#
#     time.sleep(10)


# @Then('select attribute value "{text}"')
# def step_select_conditional_attribute(context, text):
#     context.conditional_measure.select_conditional_attribute(text)
#     time.sleep(5)
#
# @Then('select condition value "{text}"')
# def select_condition_value(context, text):
#     context.conditional_measure.select_condition_value(text)
#     time.sleep(5)


@then('enter "{text}" in the attribute area')
def select_conditional_attribute(context, text):
    context.conditional_measure.select_conditional_attribute(text)
    time.sleep(5)

@then('enter "{text}" in the condition area')
def select_condition_value(context, text):
    context.conditional_measure.select_condition_value(text)
    time.sleep(5)
