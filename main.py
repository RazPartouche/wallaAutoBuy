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
# Sending keys to text box (timer is max time to search for element)
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
    fillData('//*[@id="txtUserName"]',data['email'])
    print('filled in email')
    fillData('//*[@id="txtPassword"]',data['password'])
    print('filled in pass')
    clickXpath('//*[@id="btnSubmit"]', 20)
    print('clicked on btnsubmit')
except:
    print('exception 2')

 # Navigating to product page
driver.get(data['productUrl'])

clickXpath('//*[@id="radio_1249600"]') #לא רוצה להחזיר
clickXpath('//*[@id="NewBuyBox"]/div/div[3]/div/input[1]') #לקנייה
clickXpath('//*[@id="radioShipmentMethodSelector33554436"]',20) #שליח ups
clickXpath('//*[@id="addresscon"]/ul/li/div[1]/div[2]/input[1]') #בחירת כתובת
clickXpath('//*[@id="existingPayments"]') # תשלום באשראי
clickXpath('//*[@id="creditcardtable"]/span[4]/input') #בחירת אשראי שמור במערכת
# TODO: Chose amount of payments 
fillData('//*[@id="txtUserId"]', data['taz']) #תז לאימות
### clickXpath('//*[@id="summary"]/div/div[2]/div/payment-summary/div/div[13]/input[1]')#!!אישור תשלום סופי ------------------------