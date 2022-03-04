from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s=Service('/home/martin/Документы/_PROJECTS/_PYTHON/test_behave/feature/chromedriver')
drive = webdriver.Chrome(service=s)
drive.get("http://217.9.89.223/accounts/login")
btn_login = drive.find_element(By.XPATH, "/html/body/div[3]/div/main/div[1]/div/div[3]/div/div/div/button").text
res = False
if btn_login == 'Войти':
    res = True
    print(btn_login)
    btn = drive.find_element(By.XPATH, "/html/body/div[3]/div/main/div[1]/div/div[3]/div/div/div/button")
    btn.click()

url = drive.current_url
if url.startswith("https://esiatest.mai.ru/auth/realms/demo"):
    print(f'url = true')

# I should be see "Вход в учетную запись"
sleep(2)
# enter_text = drive.find_element(By.ID, "kc-social-providers")
enter_text = drive.find_elements(By.CLASS_NAME, "text-center")
for elem in enter_text:
    if elem.text == 'Вход в учетную запись':
        res = True
# enter_text.send_keys('1')
    # print(i.get_attribute('innerHTML'))

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome("/home/martin/Документы/_PROJECTS/_PYTHON/test_behave/feature/chromedriver")
# driver.get("https://gitlab.mai.ru/")
# tit = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/h1").text
# res = False
# if tit == 'GitLab @ MAI':
#     res = True
#     print(tit)


