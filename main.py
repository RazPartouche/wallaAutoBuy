import yaml
import webbrowser
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Accessing creds.yaml
with open('creds.yaml',encoding="utf8") as file:
    data = yaml.load(file, Loader=yaml.SafeLoader)
    productUrl=(data['productUrl'])
    chromeDriverPath=(data['chromeDriverPath'])

#Clicking on elemnt when clickble (timer is max time to search for element)
def findAndClick(elementPath,timer):
    WebDriverWait(driver, timer).until(
    EC.element_to_be_clickable((By.XPATH, elementPath))).click()


#Main--------------------------------------------------------------------------------------------------------------------
driver = webdriver.Chrome(chromeDriverPath)
driver.get("https://www.wallashops.co.il/Login")

#Logging in
try: 
     driver.find_element_by_xpath('//*[@id="txtUserName"]').send_keys(data['taz'])
     driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(data['password'])
     findAndClick('//*[@id="btnSubmit"]',20)
     
except:
    print('exeption 2')


# Navigating to pruduct page
driver.get("https://www.wallashops.co.il/lenovo-thinkpad-t430-i5-240gb-ssd8gbwin-10/pi9im9im6vs9flt420i54320w7_4")
findAndClick('//*[@id="NewBuyBox"]/div/div[3]/div/input[1]',20)
# findAndClick('/html/body/div[9]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/ul/li[1]/div[2]/a',20)

# isAvailable = False
# while(isAvailable == False):
#     try:
#         findAndClick('//*[@id="NewBuyBox"]/div/div[3]/div/input[1]',20)
#     except:
#         driver.refresh()
#         continue
#     isAvailable = True


# #Adding to cart
# findAndClick('//*[@id="NewBuyBox"]/div/div[3]/div/input[1]',20)
# #checking return box
# driver.find_element_by_xpath("//input[@name='radio-button']").click()
# findAndClick('/html/body/div[6]/div/div[3]/svg/path',20)