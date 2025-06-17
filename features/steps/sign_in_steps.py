from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

VERIFY_SIGN_IN = (By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")


@then('Verify Sign in form opens')
def verify_sign_in(context):
    context.app.sign_in.verify_sign_in()