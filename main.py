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
clickXpath('//*[@id="radioShipmentMethodSelector33554436"]',20)
#todo: click on something
driver.find_element_by_xpath('//*[@id="full_name"]').send_keys(data['name'])
driver.find_element_by_xpath('//*[@id="phone"]').send_keys(data['phoneNumber'])
driver.find_element_by_xpath('//*[@id="city"]').send_keys(data['city'])
clickXpath("/html/body/ul[1]/li")
driver.find_element_by_xpath('//*[@id="street"]').send_keys(data['street'])
clickXpath("/html/body/ul[2]/li")
driver.find_element_by_xpath('//*[@id="zipcode"]').send_keys(data['zipCode'])
driver.find_element_by_xpath('//*[@id="house_no"]').send_keys(data['homeNumber'])
driver.find_element_by_xpath('//*[@id="apartment_no"]').send_keys(data['aptNumber'])
driver.find_element_by_xpath('//*[@id="floor_no"]').send_keys(data['floorNumber'])
