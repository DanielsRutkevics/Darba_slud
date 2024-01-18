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

# nodrošina, ka mājaslapa pabeigs lādties pirms turpmākām darbībām
WebDriverWait(driver, 5).until(ES.presence_of_element_located((By.CLASS_NAME, "jsx-4189752321.close-modal-button")))

# reklāmas aizvēršana
poga = driver.find_element(By.CLASS_NAME, "jsx-4189752321.close-modal-button")
poga.click()

# atvērt izvēli
poga1 = driver.find_element(By.CLASS_NAME, "css-19bqh2r")
poga1.click()
time.sleep(1)

# izvēlēties Rīgu
poga = driver.find_element(By.ID, "react-select-2-option-1-0")
poga.click()
time.sleep(1)

# atvērt izvēli
poga1 = driver.find_element(By.CLASS_NAME, "css-19bqh2r")
poga1.click()

# izvēlēties attālināti
poga2 = driver.find_element(By.ID, "react-select-2-option-0-0")
poga2.click()


# atvērt izvēli otro
uzleju = driver.find_elements(By.CLASS_NAME, "css-19bqh2r")
uzleju[1].click()
time.sleep(1)

# IT
IT = driver.find_element(By.ID, "react-select-3-option-1-0")
IT.click()
time.sleep(1)

# atķeksēt izvēles logu
kast=driver.find_element(By.CLASS_NAME, "jsx-1690969694.input-checkbox")
kast.click()
time.sleep(1)

# izvērst meklēšanas opcijas
vairak = driver.find_element(By.CLASS_NAME, "jsx-2273220519.btn-plain.btn-plain--standard")
vairak.click()
time.sleep(1)

# atvērt izvēli trešo
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


# palielināt pārlūkprogrammas logu
driver.maximize_window()
time.sleep(2)

# uzspiest rādīt rezultātus
m=driver.find_element(By.CLASS_NAME, "jsx-2818744897.search-form-footer__item")
m.click()

# izslēgt cookies
cookie=driver.find_element(By.CLASS_NAME,"cookie-consent-button")
cookie.click()

time.sleep(5)

# atjaunināt pašreizējās mājaslapas saturu
driver.refresh()

# izveido html objektu
zup= bs4.BeautifulSoup(driver.page_source,"html.parser")

# atrod visus span elementus ar noteiktu klasi
darba_nosaukumi = zup.find_all('span',class_="jsx-3024910437 vacancy-item__title")

# atver teksta failu un nolasa
with open("profesijas_sar.txt", "r") as file:
    filesat = file.read()

# ja failā nav atrastās profesijas tā tiek pievienota teksta failam
with open("profesijas_sar.txt", "a") as file:
    for darbs in darba_nosaukumi:
        if str(darbs) not in filesat:
            file.write(str(darbs.text) + "\n")



# nodrošina lai pārlūkprogramma neaizveras un var turpināt skatīties sludinājumus           
input()
