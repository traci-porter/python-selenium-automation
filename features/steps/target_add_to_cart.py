from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def safe_click(driver, by, locator, timeout=10):
    """Safely scroll to and click an element using JavaScript to avoid interception."""
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, locator))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    driver.execute_script("arguments[0].click();", element)

@when('Click the add to cart button')
def click_add_cart(context):
    safe_click(
    context.driver,
    By.CSS_SELECTOR,
    "button[aria-label*='Add V8 +Energy Summertime Watermelon']"
    )
    sleep(3)

@when('Choose options and add to cart')
def choose_options(context):
    safe_click(
    context.driver,
    By.XPATH,
     "//button[@data-test='orderPickupButton' and @id='addToCartButtonOrTextIdFor90296387']"
    )
    sleep(3)

@when('Click view cart')
def click_view_cart(context):
    print("Running 'Click view cart' step")
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'View cart')]"))
    ).click()
    sleep(3)

@then("Verify 'V8 +Energy Summertime Watermelon Energy Drink - 6pk/8 fl oz Cans' is in the cart")
def verify_product_in_cart(context):
    actual_product = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@data-test='cartItem-title']"))
    ).text

    expected = "V8 +Energy Summertime Watermelon Energy Drink - 6pk/8 fl oz Cans".lower().strip()
    actual = actual_product.lower().strip()
    assert expected in actual, f'Expected product "{expected}" not found in cart. Found "{actual_product}" instead.'

    #assert product.lower() in actual_product.lower(), f'Expected product "{product}" not found in cart item "{actual_product}".'

    #expected = product.lower().strip()
    #actual = actual_product.lower().strip()

    #assert expected in actual, f'Error: Expected "{product}" but found "{actual_product}" in the cart.'

#    actual_product = context.driver.find_element(By.XPATH, "//div[@data-test='cartItem-title']").text

#    expected = product.lower().strip()
#    actual = actual_product.lower().strip()

#   assert expected in actual, f'Error, expected product \"{product}\" not found in cart item \"{actual_product}\"'
