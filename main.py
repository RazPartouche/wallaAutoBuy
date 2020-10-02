import yaml
import webbrowser
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Accessing creds.yaml
with open('creds.yaml', encoding="utf8") as file:
    data = yaml.load(file, Loader=yaml.SafeLoader)
    # productUrl = (data['productUrl'])
    chromeDriverPath = (data['chromeDriverPath'])

# Clicking on element when clickable (timer is max time to search for element)


def clickXpath(elementPath, timer=20):
    WebDriverWait(driver, timer).until(EC.element_to_be_clickable((By.XPATH, elementPath))).click()

def fillData(elementPath,keys, timer=20):
    WebDriverWait(driver, timer).until(EC.element_to_be_clickable((By.XPATH, elementPath))).send_keys(keys)

# Main--------------------------------------------------------------------------------------------------------------------

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromeDriverPath )
driver.get("https://www.wallashops.co.il/Login")

# Logging in
try:
    driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(data['email'])
    print('filled in taz')
    driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(data['password'])
    print('filled in pass')
    clickXpath('//*[@id="btnSubmit"]', 20)
    print('filled in btnsubmit')
except:
    print('exception 2')

 # Navigating to pruduct page
driver.get(data['productUrl'])

# time.sleep(5)
clickXpath('//*[@id="radio_1249600"]') #לא רוצה להחזיר
clickXpath('//*[@id="NewBuyBox"]/div/div[3]/div/input[1]') #לקנייה
clickXpath('//*[@id="radioShipmentMethodSelector33554436"]',20) #שליח ups
clickXpath('//*[@id="addresscon"]/ul/li/div[1]/div[2]/input[1]') #בחירת כתובת
clickXpath('//*[@id="existingPayments"]') # תשלום באשראי

driver.switch_to.frame(0)#Swhitch to credit card frame
fillData('//*[@id="userData2"]',data['name'])
fillData('//*[@id="cardNumber"]',data['creditCard'])
fillData('//*[@id="personalId"]',data['taz'])


