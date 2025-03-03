import time
from behave import given
from selenium import webdriver  # ✅ Import WebDriver to restart it
from pages.dqlogin_page import LoginPage
from utils.credential_loader import load_credentials

@given("I login with multiple credentials, skipping failed logins")
def step_impl(context):
    """Iterate through multiple credentials and retry login if failed."""

    # Load credentials from JSON
    credentials = load_credentials("configs/dqlogin_users.json")

    for index, cred in enumerate(credentials):
        username = cred["username"]
        password = cred["password"]

        print(f"🔹 Attempting login {index + 1} with {username}")

        #✅ Start a new browser instance for each credential
        context.driver = webdriver.Chrome()  # 🔥 Reinitialize WebDriver
        context.driver.maximize_window()
        context.driver.implicitly_wait(5)

        login_page = LoginPage(context.driver)
        login_page.load_login_page(context.base_url)
        login_page.login(username, password)

        time.sleep(5)

        # ✅ If login fails, restart browser before next credential
        if login_page.is_login_failed():
            print(f"🚨 Login failed for {username}. Skipping to next credential.")
            context.driver.quit()  # ❌ Closes browser
            continue  # ✅ Move to next credential

        # ✅ If last credential, do NOT close browser
        if index == len(credentials) - 1:
            print("✅ Login successful with last credential. Keeping browser open.")
        else:
            print(f"🔄 Closing browser for {username} and moving to next attempt.")
            context.driver.quit()  # ✅ Close browser


# import time
# from behave import given
# from selenium import webdriver  # ✅ Import WebDriver to restart it
# from pages.dqlogin_page import LoginPage
# from utils.credential_loader import load_credentials
#
# @given("I login with multiple credentials, skipping failed logins")
# def step_impl(context):
#     """Iterate through multiple credentials and retry login if failed."""
#
#     # Load credentials from JSON
#     credentials = load_credentials("configs/dqlogin_users.json")  # ✅ Adjust path if needed
#
#     for index, cred in enumerate(credentials):
#         username = cred["username"]
#         password = cred["password"]
#
#         print(f"🔹 Attempting login {index + 1} with {username}")
#
#         # # ✅ Start a new browser instance for each credential
#         # context.driver = webdriver.Chrome()  # 🔥 Reinitialize WebDriver
#         # context.driver.maximize_window()
#         # context.driver.implicitly_wait(5)
#
#         login_page = LoginPage(context.driver)
#         login_page.load_login_page(context.base_url)
#
#         login_page.login(username, password)
#
#         time.sleep(5)
#
#         # ✅ If login fails, close browser and continue to next credential
#         if login_page.is_login_failed():
#             print(f"🚨 Login failed for {username}. Skipping to next credential.")
#             context.driver.quit()
#             continue  # Move to the next credential
#
#         # ✅ If last credential, do NOT close browser
#         if index == len(credentials) - 1:
#             print("✅ Login successful with last credential. Keeping browser open.")
#         else:
#             print(f"🔄 Closing browser for {username} and moving to next attempt.")
#             context.driver.quit()  # Close browser before next attempt

