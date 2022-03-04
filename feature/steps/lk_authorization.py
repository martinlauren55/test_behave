from time import sleep, time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@when(u'I visit page "{url}"')
def step_impl(context, url):
    try:
        context.driver.get(url)
    except:
        assert False
    assert True


@when(u'Click on btn "{name}"')
def step_impl(context, name):
    btn_login = context.driver.find_element(By.XPATH,
                                            "/html/body/div[3]/div/main/div[1]/div/div[3]/div/div/div/button").text
    res = False
    if btn_login == name:
        btn = context.driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div[1]/div/div[3]/div/div/div/button")
        btn.click()
        res = True
    assert res is True


@then(u'I should be redirected to Keycloak authorization link started with "{url}"')
def step_impl(context, url):
    sleep(2)
    try:
        current_url = context.driver.current_url
        if current_url.startswith(url):
            assert True
    except:
        assert False


@then(u'I should be see title "{title}"')
def step_impl(context, title):
    try:
        if title == context.driver.find_element(By.ID, "kc_loginAccountTitleForm").text:
            assert True
    except:
        assert False


@when(u'I fill email "{email}" and password "{pasw}"')
def step_impl(context, email, pasw):
    try:
        context.driver.find_element(By.ID, "username").send_keys(email)
        context.driver.find_element(By.ID, "password").send_keys(pasw)
    except:
        assert False
    assert True


@when(u'Click on Keycloak btn "{name}"')
def step_impl(context, name):
    try:
        context.driver.find_element(By.ID, "kc-login").click()
        assert True
    except:
        assert False
