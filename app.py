import json
import time

import Flask as Flask
from pip._vendor import requests
from db import read, insert, insertUserId, readUsers

size = 0
name = "Lviv"
key = "c09888259b05a470a1e1d99d48c9b887"
api = "https://api.telegram.org/bot1173766879:AAEDlHiaVmLMsu2EmH3y9Royn1wrJRoc8vk/"
from selenium import webdriver
import os
def getTemperature():
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?q=" + name + "&appid=" + key + "&units=metric"
    r = requests.get(baseUrl)
    print(r.text)
    y = json.loads(r.text)
    result = y["main"]["temp"]
    return result
def sendMessage(chatid, message):
    r = requests.get(api + "sendMessage?chat_id=" + str(chatid) + "&text=" + message)

def getUpdate():
    result = requests.get(api + "getUpdates")
    return result.text


def welcomeAnswer():
    global size
    data = json.loads(getUpdate())

    messages = data["result"]
    for i in range(size, len(messages)):
        userMsg = messages[i]['message']["text"]
        chatid = messages[i]['message']['chat']['id']
        name = messages[i]['message']["chat"]["first_name"]
        if userMsg == "/start":
            print("новые пользователи исследованы")
            insertUserId(chatid, name)
    size = len(messages)


def mailing(link):
    users = readUsers()
    for i in users:
        sendMessage(i[0], link)


def csgomatches():
    PROXY = "138.197.105.27:3128	"  # IP:PORT or HOST:PORT
    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    op.add_argument("--headless")
    op.add_argument("--disable-dev-sh-usage")
    op.add_argument("--no-sandbox")
    op.add_argument('--ignore-certificate-errors')
    op.add_argument('--incognito')
    op.add_argument('--proxy-server=%s' % PROXY)

    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
    # driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=op)

    driver.get('https://www.hltv.org/')
    cont = driver.find_element_by_class_name("standard-list")

    links = cont.find_elements_by_tag_name("a")#

    arr = read()
    print(len(links))
    print(len(arr))
    for i in links:
        isPresent = False
        for k in arr:
            if k[0] == i.get_attribute("href"):
                isPresent = True
                break
        if isPresent == False:  #
            sendMsgs(i.get_attribute("href")) #
            insert(i.get_attribute("href"))  #

    driver.quit()

def sendMsgs(msg):
    usersId = readUsers()
    for i in usersId:
        sendMessage(str(i[0]), msg)


app = Flask(__name__)


while True:
    print("идем парсить")
    csgomatches()
    print("запарсено")
    print("идем за новыми падованами")

    welcomeAnswer()

    time.sleep(16.4)

