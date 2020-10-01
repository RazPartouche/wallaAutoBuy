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


def findAndClick(elementPath, timer):
    WebDriverWait(driver, timer).until(
        EC.element_to_be_clickable((By.XPATH, elementPath))).click()


# Main--------------------------------------------------------------------------------------------------------------------
driver = webdriver.Chrome(chromeDriverPath)
driver.get("https://www.wallashops.co.il/Login")

# Logging in
try:
    driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(data['email'])
    print('filled in taz')
    driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(data['password'])
    print('filled in pass')
    findAndClick('//*[@id="btnSubmit"]', 20)
    print('filled in btnSubmit')
except:
    print('exception 2')

 # Navigating to pruduct page
driver.get("https://www.wallashops.co.il/lenovo-thinkpad-t430-i5-240gb-ssd8gbwin-10/pi9im9im6vs9flt420i54320w7_4")
findAndClick('//*[@id="NewBuyBox"]/div/div[3]/div/input[1]',20)
time.sleep(5)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="radio_1249600"]'))).click()
findAndClick('/html/body/div[7]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/ul/li[1]/div[2]/a',20) #not working as of right now, seems like the xpath is dynamic
# /html/body/div[7]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/ul/li[1]/div[2]/a
findAndClick('//*[@id="updatebtn"]',20)
findAndClick('//*[@id="radioShipmentMethodSelector33554436"]',20)
driver.find_element_by_xpath('//*[@id="full_name"]').send_keys(data['name'])
driver.find_element_by_xpath('//*[@id="phone"]').send_keys(data['phoneNumber'])
driver.find_element_by_xpath('//*[@id="city"]').send_keys(data['city'])
driver.find_element_by_xpath('//*[@id="street"]').send_keys(data['street'])
driver.find_element_by_xpath('//*[@id="zipcode"]').send_keys(data['zipCode'])
# driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(data['aptNumber'])
# driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(data['homeNumber'])
