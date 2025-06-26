from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'][id*='addToCart']")
SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper']h4")

#@when('Click on Add to Cart button')
#def click_add_to_cart(context):
#    context.driver.find_element(*ADD_TO_CART_BTN).click()
#    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME), message='Product name was not visible')
    #   sleep(3)


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored:' ',context.product_name')

#@when('Confirm Add to Cart button from side navigation')
#def side_nav_click_add_to_cart(context):
#    context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN)).click()

@when('Hover favorites icon')
def hover_fav_icon(context):
    context.app.search_results_page.hover_fav_icon()

@then('Verify search worked for {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)

@then('Favorites tooltip is shown')
def verify_fav_tt_shown(context):
    context.app.search_results_page.verify_fav_tt_shown()

@then('Verify cart is empty')
def cart_is_empty(context):
    context.app.search_results_page.cart_is_empty()

