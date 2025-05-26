from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#init driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
driver.get('https://target.com')

# Target product

driver.find_element(By.ID, 'search').send_keys('pencil')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(3)

# verification
expected_text = 'pencil'
actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text

assert expected_text in actual_text, f'Error, expected {expected_text} not in actual {actual_text}'
print('Test case passed')

sleep(5)
driver.quit()