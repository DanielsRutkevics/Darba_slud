import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options= option)

url = "https://cv.lv/lv"
driver.get(url)
poga = driver.find_element(By.CLASS_NAME, "jsx-4189752321.close-modal-button")
poga.click()





input()

