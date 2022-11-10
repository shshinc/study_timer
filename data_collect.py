from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
def selenium_scroll_option():
    SCROLL_PAUSE_SEC = 3

    # 스크롤 높이 가져옴
    last_height = driver.execute_script("return document.body.scrollHeight")


chrome_options = webdriver.ChromeOptions()
base_url = "https://www.google.co.kr/imghp?hl=ko"
word = "pen"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(base_url)
browser = driver.find_element(By.NAME, "q")
browser.send_keys(word)
browser.send_keys(Keys.RETURN)

seleniu,_scroll_option()