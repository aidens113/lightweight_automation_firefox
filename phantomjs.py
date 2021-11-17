import pyautogui
import time
import math
import random
import os
import sys
import requests
import wmi
import imaplib
import email
from email.header import decode_header
import webbrowser
import threading
from os.path import expanduser
import concurrent.futures
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from os.path import expanduser
import concurrent.futures
from datetime import datetime
import time,string,zipfile,os
import selenium
import base64
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

trafficdelivered = 0

def press_key(key, driver):
    actions = ActionChains(driver)
    actions.send_keys(key)
    actions.perform()

def randkeys(element, keys, driver):
    for myi in keys:
        element.send_keys(myi)
        time.sleep(random.uniform(0.05, 0.25))

        
def initdriver():
    options2 = Options()
    #options2.headless = True


    proxy = "proxyhere"

    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True

    firefox_capabilities['proxy'] = {
        "proxyType": "MANUAL",
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy
    }

    driver = webdriver.Firefox(proxy=proxy,capabilities=firefox_capabilities,options=options2,executable_path="geckodriver.exe",)
    return driver


def setreferer(request):
    del request.headers['Referer']
    sources = ['https://google.com','https://instagram.com','https://facebook.com','https://yahoo.ca','https://bing.com','duckduckgo.com'] 
    
    request.headers['Referer'] = sources[random.randint(0,int(len(sources)-1))]
    

def go():
    global trafficdelivered
    global websiteglobal
    file = open("useragents.txt","r")
    useragents = file.readlines()
    file.close()
    
    while True:
        #useragent = str(useragents[random.randint(0,int(len(useragents)-1))]).replace("\n","").replace("\r","")           
        #element = driver.find_element_by_id('test')
        try:
            for _ in range(10):
                try:
                    driver = initdriver()
                    break
                except Exception as EEeee:
                    print("Error: "+str(EEeee))

            
            for _ in range(10):
                try:
                    driver.get(websiteglobal)
                    break
                except:
                    print("Err")
            time.sleep(1)

            for _ in range(10):
                try:
                    driver.find_element_by_id('test').click()
                    #break
                    time.sleep(0.5)
                except:
                    print("Error clicking")
            time.sleep(20)
            try:
                driver.close()
                driver.quit()
            except:
                print("Error closing driver")
            
        except Exception as EEeer:
            print("Tried to click failed: "+str(EEeer))
            try:
                driver.close()
                driver.quit()
            except:
                print("Error closing driver")
        trafficdelivered += 1


def updatethread():
    global trafficdelivered
    while True:
        try:
            print("Lightweight Firefox Traffic Delivery")
            print("------------------------------------")
            print("Traffic Delivered: "+str(trafficdelivered))
            time.sleep(1)
            os.system('cls')
        except Exception as EE:
            print("Error: "+str(EE))

            
def startthreads(threadnum):
    
    threads = []
    #file = open("proxies.txt","r")
    #proxies = file.readlines()
    #file.close()

    thread = threading.Thread(target=updatethread)
    thread.start()
    
    for i in range(threadnum):
        Thread = threading.Thread(target=go)    
        threads.append(Thread)
    for thread in threads:
        thread.start()
        time.sleep(random.uniform(5.0, 15.0))
    for thread in threads:
        thread.join()

    
print("""
WELCOME TO TRAFFICBOT V.1
drive super lightweight bot traffic to any website with high quality proxies
-
""")
websiteglobal = "https://yourwebsitehere.com"
threadstodo = int(input("Threads: "))

startthreads(threadstodo)

print("Beginning organic style traffic flow with high quality scrolling and clicking")
    


