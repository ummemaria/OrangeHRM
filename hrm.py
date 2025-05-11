from time import sleep
from cred import Username, Password
from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False, args = ["--start-maximized"], slow_mo=500)
    context = browser. new_context(no_viewport = True,
                                   
        storage_state = "playwright/.auth/storage_state.json"
                                   
                                   )
    page = context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login Credentials
    # user_field = page.get_by_placeholder("Username")
    # user_field.fill(Username)

    # password_field = page.get_by_placeholder("Password")
    # password_field.fill(Password)

    # #Click on the login button

    # login_click = page.get_by_role("button", name=" Login")
    # login_click.click()

    #auth save
    # context.storage_state(path = "playwright/.auth/storage_state.json")

    #Click on the leave module

    # leave_module = page.get_by_role('link', name= "Leave")
    # leave_module.click()

    # #click on the leave apply feature

    # leave_apply = page.get_by_role('link', name= "Apply")
    # leave_apply.click()


    sleep(2)


    page.close()
    