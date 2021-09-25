#setup selenium
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.support import expected_conditions as EC
import time
from mains import *
from threading import Thread

driver = webdriver.Firefox(executable_path="C:\dr\geckodriver.exe")
#maximize chrome
driver.maximize_window()

#open tiktok
driver.get("https://www.tiktok.com/login/phone-or-email/email")


#login
gg = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[2]/div[1]')
gg.click()
name = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/form/div[1]/input')
time.sleep(2)
name.send_keys("hakantanc2")
password = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/form/div[2]/input')
time.sleep(2)
password.send_keys("123456tr.")
#press login  button
login = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/form/button')
login.click()
#wait for the login button to appear
time.sleep(2)

Thread(target=main_loop).start()
