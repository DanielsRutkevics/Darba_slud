import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options= option)

url = "https://cv.lv/lv"
driver.get(url)
WebDriverWait(driver, 5).until(ES.presence_of_element_located((By.CLASS_NAME, "jsx-4189752321.close-modal-button")))


poga = driver.find_element(By.CLASS_NAME, "jsx-4189752321.close-modal-button")
poga.click()
poga1 = driver.find_element(By.CLASS_NAME, "css-19bqh2r")
poga1.click()
time.sleep(3)
poga = driver.find_element(By.ID, "react-select-2-option-1-0")
poga.click()
time.sleep(1)
uzleju = driver.find_elements(By.CLASS_NAME, "css-19bqh2r")
print(uzleju)
uzleju[1].click()
time.sleep(1)
IT = driver.find_element(By.ID, "react-select-3-option-1-0")
IT.click()
time.sleep(1)
kast=driver.find_element(By.CLASS_NAME, "jsx-1690969694.input-checkbox")
kast.click()
time.sleep(1)
vairak = driver.find_element(By.CLASS_NAME, "jsx-2273220519.btn-plain.btn-plain--standard")
vairak.click()
meklēt=driver.find_element(By.XPATH, '//button[contains(span, "Rādīt")]')
meklēt.click()

input()
time.sleep(4)

