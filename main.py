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


def telegramNotify(msg):
    token = data['telegramToken']
    userId = data['telegramIdToNotify']
    msgUrl = "https://api.telegram.org/bot"+token + \
        "/sendMessage?chat_id="+userId+"&text="+msg
    requests.get(msgUrl)
    print(msgUrl)
    return True


def screenshotAndSend():
    currentTime = time.strftime("%H.%M.%S", time.localtime())
    imgPath = 'screenshot-'+currentTime+".png"
    driver.save_screenshot(imgPath)
    print('Taking screenshot')

    url = "https://api.telegram.org/bot"+data['telegramToken']+"/sendPhoto"
    files = {'photo': open(imgPath, 'rb')}
    dataToSend = {'chat_id': data['telegramIdToNotify']}
    requests.post(url, files=files, data=dataToSend)
    print('Image sent')

# Clicking on element when clickable (timer is max time to search for element)


def clickXpath(elementPath, timer=20):
    WebDriverWait(driver, timer).until(
        EC.element_to_be_clickable((By.XPATH, elementPath))).click()


def waitXpath(elementPath, timer=20):
    WebDriverWait(driver, timer).until(
        EC.element_to_be_clickable((By.XPATH, elementPath)))
# Sending keys to text box (timer is max time to search for element)


def fillData(elementPath, keys, timer=20):
    WebDriverWait(driver, timer).until(
        EC.element_to_be_clickable((By.XPATH, elementPath))).send_keys(keys)

def main():
    # Navigating to product page
    driver.get(data['productUrl'])

    waitXpath('//*[@id="NewBuyBox"]/div/div[3]/div/input[1]')
    try:
        clickXpath('//*[@id="radio_1249600"]', 2)  # לא רוצה להחזיר
    except:
        print("Couldn't find don't want to return box")
    clickXpath('//*[@id="NewBuyBox"]/div/div[3]/div/input[1]')  # לקנייה
    try:
        # עדכן לאחר הקנייה, לא אמור להופיע
        clickXpath('//*[@id="updatebtn"]', 1)
    except:
        print("Couldn't find updatebtn")
    #we get sleep from the updatebtn because it most likely ain't going to show up
    try:
        clickXpath('//*[@id="radioShipmentMethodSelector4"]', 10)  # שליח חינם
    except:
        # שליח ups
        clickXpath('//*[@id="radioShipmentMethodSelector33554436"]')

    # בחירת כתובת
    clickXpath('//*[@id="addresscon"]/ul/li/div[1]/div[2]/input[1]')
    clickXpath('//*[@id="existingPayments"]')  # תשלום באשראי
    # בחירת אשראי שמור במערכת
    clickXpath('//*[@id="creditcardtable"]/span[4]/input')
    clickXpath('//*[@id="txtpayment"]/option[2]')  # תשלומים
    fillData('//*[@id="txtUserId"]', data['taz'])  # תז לאימות
    # #Final payment
    # ### clickXpath('//*[@id="summary"]/div/div[2]/div/payment-summary/div/div[13]/input[1]')#!!אישור תשלום סופי ------------------------
    telegramNotify("Congratz! you got the product and will most likely get a picture of the purchase in 15 seconds")
    time.sleep(15) # sleep in order to acount for purchesing time before screenshot
    screenshotAndSend()


# Main--------------------------------------------------------------------------------------------------------------------
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path=chromeDriverPath)
driver.get("https://www.wallashops.co.il/Login")

# Logging in
fillData('//*[@id="txtUserName"]', data['email'])
print('filled in email')
fillData('//*[@id="txtPassword"]', data['password'])
print('filled in pass')
clickXpath('//*[@id="btnSubmit"]', 20)
print('clicked on btnsubmit')

tryCounter = 1
while True:
    print("Trying to run the script for  the {}nd time".format(tryCounter))
    # with open('status.txt') as f:
    #     statusLine = f.readline()
    # print(statusLine)
    try:
        main()
    except:
        tryCounter += 1
        continue
    exit(0)



