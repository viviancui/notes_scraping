from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/viviancui/Desktop/selenium_practice/drivers/chromedriver")

driver.set_page_load_timeout(10)
driver.get("http://google.com")
#we can find_element or find_elements
#we can find_element_by_id, by class name, by tag name, by name, by link text, by partial link text, by css, by XPath, by javascript
driver.find_element_by_name("q").send_keys("Automation Step by Step")

# driver.find_element_by_name("btnK").click()
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

#Here is another method to enter the keys
# submit the form (although google automatically searches now without submitting)
# inputElement.submit()

time.sleep(4)
driver.quit()
