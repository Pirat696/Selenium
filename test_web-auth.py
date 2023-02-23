import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


url = "https://domofon.mts.ru/"
browser = webdriver.Chrome()

try:
    browser.get(url=url)
    email_input = browser.find_element(By.NAME, "username")
    email_input.click()
    email_input.send_keys("username")
    email_input = browser.find_element(By.NAME, "password")
    email_input.click()
    email_input.send_keys("password")
    email_input.send_keys(Keys.ENTER)
    time.sleep(5)

except Exception as e:
    print(e)
finally:
    browser.close()
    browser.quit()
