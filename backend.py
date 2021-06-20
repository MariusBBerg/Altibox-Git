from splinter import Browser
from selenium import webdriver
import download
import time
import json
import os
import shutil

def switch_cred(username_config, password_config):
    if os.path.isfile('./config.json') == False:
        data = {
            "username": "",
            "password": ""
            }
        file = json.dumps(data)
        with open("config.json", "w") as jsonfile:
            jsonfile.write(file)


    with open("config.json", "r") as f:
        data = json.load(f)
        f.close()
    
    data['username']=username_config
    data['password']=password_config

    with open("config.json", "w") as f:
        myJSON = json.dump(data, f)
        f.close()



def switch(username,password):


    

    executable_path= {'executable_path':r'C:\temp\AltiboxApp\chromedriver'}

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    options.add_argument("--disable-notifications")

    browser = Browser('chrome', **executable_path, headless = False, options = options)

    browser.visit("https://www.altibox.no/minesider/")


    username_box = browser.find_by_id('username')

    username_box.fill(username)

    password_b = browser.find_by_id('password').fill(password)

    browser.find_by_xpath('//*[@id="login"]/div[3]/div/form/div/span/input').click()

    browser.find_by_id('wp-').click()

    browser.find_by_xpath('//*[@id="content"]/div[3]/div/div[1]/div/section/ul/li[1]/a').click()


    #FJERNER/Legger til TV2SPORT
    browser.find_by_xpath('//*[@id="focContent"]/div[5]/div/div/div[1]').click()
    browser.find_by_xpath('//*[@id="focModal"]/div/div/div/div/div[1]/div[5]/button').click()

    time.sleep(1)
    #FJERNER/legger til EUROSPORT
    browser.find_by_xpath('//*[@id="focContent"]/div[5]/div/div/div[2]').click()
    browser.find_by_xpath('//*[@id="focModal"]/div/div/div/div/div[1]/div[5]/button').click()

    time.sleep(1)
    #Fjerner/legger til viaplay
    browser.find_by_xpath('//*[@id="focContent"]/div[5]/div/div/div[3]').click()
    browser.find_by_xpath('//*[@id="focModal"]/div/div/div/div/div[1]/div[5]/button').click()

    time.sleep(1)
    #Fjerner/legger til Nordisk film
    browser.find_by_xpath('//*[@id="focContent"]/div[5]/div/div/div[11]').click()
    browser.find_by_xpath('//*[@id="focModal"]/div/div/div/div/div[1]/div[5]/button').click()

    time.sleep(1)
    #LAGRER
    browser.find_by_xpath('//*[@id="focContent"]/div[2]/div[1]/button').click()

    time.sleep(1)

    browser.quit()

def delete():
    shutil.rmtree("C:/temp/AltiboxApp/")



