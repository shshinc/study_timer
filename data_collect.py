from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

chrome_options = webdriver.ChromeOptions()
base_url = "https://www.google.co.kr/imghp?hl=ko"
word = "pen"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(base_url)
browser = driver.find_element(By.NAME, "q")
browser.send_keys(word)
browser.send_keys(Keys.RETURN)