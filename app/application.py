from pages.base_page import Page
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.sign_in = SignInPage(driver)

#app = Application()
#app.main_page.open_main_page()
#app.header.search_product()
