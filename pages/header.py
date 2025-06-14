from features.steps.header_steps import SEARCH_FIELD
from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


    def search_product(self):
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

