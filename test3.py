from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s=Service('/home/martin/Документы/_PROJECTS/_PYTHON/test_behave/feature/chromedriver')
drive = webdriver.Chrome(service=s)

####################################
drive.get("https://esiatest.mai.ru/auth/realms/demo/account/")
sleep(4)
t = drive.find_element(By.ID, "kc_loginAccountTitleForm").text
print(f'*{t}*')