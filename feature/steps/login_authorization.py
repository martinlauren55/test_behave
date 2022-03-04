from time import sleep

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




# @given(u'lunched chrome browser')
# def step_impl(context):
#     s = Service(r'C:\CLOUDS\apollonkacity@gmail.com\test_behave\chromedriver_98.0.4758.80/chromedriver.exe')
#     context.driver = webdriver.Chrome(service=s)

@when(u'open site lk')
def step_impl(context):
    context.driver.get("http://217.9.89.223/accounts/login")


@when(u'click on btns "Войти"')
def step_impl(context):
    btn_login = context.driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div[1]/div/div[3]/div/div/div/button").text
    res = False
    if btn_login == 'Войти':
        btn = context.driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div[1]/div/div[3]/div/div/div/button")
        btn.click()
        res = True
    assert res is True


@then(u'I should be redirected to Keycloak authorizations')
def step_impl(context):
    sleep(2)
    url = context.driver.current_url
    res = False
    if url.startswith("https://esiatest.mai.ru/auth/realms/demo/"):
        res = True
    assert res is True
    # assert url.startswith("https://esiatest.mai.ru/auth/realms/demo/")


@then(u'I should be see "Вход в учетную запись"')
def step_impl(context):
    enter_text = context.driver.find_elements(By.CLASS_NAME, "text-center")
    res = False
    for elem in enter_text:
        if elem.text == 'Вход в учетную запись':
            res = True
    assert res is True



