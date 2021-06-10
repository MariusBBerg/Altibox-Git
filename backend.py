from splinter import Browser
from selenium import webdriver
import download
import time
import os
import shutil

def switch(username,password):

    executable_path= {'executable_path':r'C:\temp\AltiboxApp\chromedriver'}

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    options.add_argument("--disable-notifications")

    browser = Browser('chrome', **executable_path, headless = True, options = options)

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

    time.sleep(3)
    #FJERNER/legger til EUROSPORT
    browser.find_by_xpath('//*[@id="focContent"]/div[5]/div/div/div[2]').click()
    browser.find_by_xpath('//*[@id="focModal"]/div/div/div/div/div[1]/div[5]/button').click()

    time.sleep(3)
    #Fjerner/legger til viaplay
    browser.find_by_xpath('//*[@id="focContent"]/div[5]/div/div/div[3]').click()
    browser.find_by_xpath('//*[@id="focModal"]/div/div/div/div/div[1]/div[5]/button').click()

    time.sleep(3)
    #Fjerner/legger til Nordisk film
    browser.find_by_xpath('//*[@id="focContent"]/div[5]/div/div/div[10]').click()
    browser.find_by_xpath('//*[@id="focModal"]/div/div/div/div/div[1]/div[5]/button').click()

    time.sleep(3)
    #LAGRER
    browser.find_by_xpath('//*[@id="focContent"]/div[2]/div[1]/button').click()

    time.sleep(3)

    browser.quit()

def delete():
    shutil.rmtree("C:/temp/AltiboxApp/")



