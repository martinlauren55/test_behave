from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print(u'> lunched chrome browser')
s = Service(r'C:\CLOUDS\apollonkacity@gmail.com\test_behave\chromedriver_98.0.4758.80/chromedriver.exe')
driver = webdriver.Chrome(service=s)

print(u'> open site lk')
driver.get("http://217.9.89.223/accounts/login")

print(u'> click on btn "Войти"')
btn_login = driver.find_element(By.XPATH,
                                        "/html/body/div[3]/div/main/div[1]/div/div[3]/div/div/div/button").text
res = False
if btn_login == 'Войти':
    btn = driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div[1]/div/div[3]/div/div/div/button")
    btn.click()
    print("Войти = yes")


print(u'> I should be redirected to keykloak authorization')
sleep(3)
url = driver.current_url
res = False
if url.startswith("https://esiatest.mai.ru/auth/realms/demo/"):
    print('domen "https://esiatest.mai.ru" = yes')


print(u'> I should be see "Вход в учетную запись"')
enter_text = driver.find_elements(By.CLASS_NAME, "text-center")
res = False
for elem in enter_text:
    if elem.text == 'Вход в учетную запись':
        print('Вход в учетную запись = yes')
