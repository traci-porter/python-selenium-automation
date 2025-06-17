from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Page:
    def __init__(self, driver):
        self.driver = driver


    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    #def click(self, *locator):
    #    self.driver.find_element(*locator).click()

    def click(self, by, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, locator)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except Exception as e:
            print(f"Click intercepted: {e}, trying JS click")
            self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text