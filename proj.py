import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import time
import bs4

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
time.sleep(1)
poga = driver.find_element(By.ID, "react-select-2-option-1-0")
poga.click()
time.sleep(1)
poga1 = driver.find_element(By.CLASS_NAME, "css-19bqh2r")
poga1.click()
poga2 = driver.find_element(By.ID, "react-select-2-option-0-0")
poga2.click()



uzleju = driver.find_elements(By.CLASS_NAME, "css-19bqh2r")
uzleju[1].click()
time.sleep(1)

IT = driver.find_element(By.ID, "react-select-3-option-0-0")
IT.click()
time.sleep(1)

kast=driver.find_element(By.CLASS_NAME, "jsx-1690969694.input-checkbox")
kast.click()
time.sleep(1)

vairak = driver.find_element(By.CLASS_NAME, "jsx-2273220519.btn-plain.btn-plain--standard")
vairak.click()
time.sleep(1)

zleju = driver.find_elements(By.CLASS_NAME, "css-19bqh2r")
zleju[4].click()
time.sleep(3)
pus= driver.find_element(By.ID, "react-select-5-option-2")
pus.click()
time.sleep(3)
zleju = driver.find_elements(By.CLASS_NAME, "css-19bqh2r")
zleju[4].click()
pecmac = driver.find_element(By.ID, "react-select-5-option-4")
pecmac.click()
zleju = driver.find_elements(By.CLASS_NAME, "css-19bqh2r")
zleju[4].click()
prakse = driver.find_element(By.ID, "react-select-5-option-5")
prakse.click()



driver.maximize_window()
time.sleep(2)

m=driver.find_element(By.CLASS_NAME, "jsx-2818744897.search-form-footer__item")
m.click()

cookie=driver.find_element(By.CLASS_NAME,"cookie-consent-button")
cookie.click()


time.sleep(5)
# WebDriverWait(driver, 5).until(ES.presence_of_element_located((By.CLASS_NAME, "jsx-4189752321.close-modal-button")))
# # url2 = "https://cv.lv/lv/search?limit=20&offset=0&categories%5B0%5D=INFORMATION_TECHNOLOGY&workTimes%5B0%5D=PART_TIME&workTimes%5B1%5D=WORK_AFTER_CLASSES&workTimes%5B2%5D=PRACTICE&towns%5B0%5D=543&fuzzy=false&suitableForRefugees=false&isHourlySalary=false&isRemoteWork=true&isQuickApply=false"
# # saturs = requests.get(url2)
driver.refresh()
zup= bs4.BeautifulSoup(driver.page_source,"html.parser")

darba_nosaukumi = zup.find_all('span',class_="jsx-3024910437 vacancy-item__title")

with open("profesijas_sar.txt", "r") as file:
    filesat = file.read()

with open("profesijas_sar.txt", "a") as file:
    for darbs in darba_nosaukumi:
        if str(darbs) not in filesat:
            file.write(str(darbs.text) + "\n")



            
input()
