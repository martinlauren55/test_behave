from time import sleep

from behave import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import ntpath
import os


def before_all(context):
    # s = Service(r'C:\CLOUDS\apollonkacity@gmail.com\test_behave\chromedriver_98.0.4758.80/chromedriver.exe') # for win
    path_to_driver = os.path.join(ntpath.dirname(__file__), os.path.join("chromedriver"))
    s = Service(path_to_driver)   # for lin
    # options = webdriver.ChromeOptions() # for win
    # options.add_experimental_option('excludeSwitches', ['enable-logging']) # for win
    # context.driver = webdriver.Chrome(service=s,options=options) # for win
    context.driver = webdriver.Chrome(service=s)   # for lin
