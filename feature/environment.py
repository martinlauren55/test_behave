from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def before_all(context):
    # s = Service(r'C:\CLOUDS\apollonkacity@gmail.com\test_behave\chromedriver_98.0.4758.80/chromedriver.exe') # for win
    s = Service("/home/martin/Загрузки/Telegram Desktop/test_behave/feature/chromedriver") # for lin
    # options = webdriver.ChromeOptions() # for win
    # options.add_experimental_option('excludeSwitches', ['enable-logging']) # for win
    # context.driver = webdriver.Chrome(service=s,options=options) # for win
    context.driver = webdriver.Chrome(service=s) # for lin
