from features.steps.header_steps import SEARCH_FIELD, CART_ICON
from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    VERIFY_SIGN_IN = (By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")

    def verify_sign_in(self):
        actual_text = self.find_element(*self.VERIFY_SIGN_IN).text
        expected_text = 'Sign in or create account'
        assert actual_text == expected_text, f"Error, expected {expected_text} but got actual {actual_text}"