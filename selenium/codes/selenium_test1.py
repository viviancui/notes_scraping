from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/viviancui/Desktop/selenium_practice/drivers/chromedriver")

driver.set_page_load_timeout(10)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation Step by Step")
# driver.find_element_by_name("btnK").click()
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()
