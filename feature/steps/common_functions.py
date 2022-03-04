from time import sleep, time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# @when(u'Click on Button name: "{name}" element By ID: "{elem_id}"')
# def click_btn_id(context, name, elem_id):
#     try:
#         btn_name = context.driver.find_element(By.ID, elem_id).text
#         if btn_name == name:
#             context.driver.find_element(By.ID, elem_id).click()
#             assert True
#     except:
#         assert False


# @when(u'Click on Button name: "{name}" element By XPATH: "{xpath}"')
# def click_btn_xpath(context, name, xpath):
#     try:
#         btn_name = context.driver.find_element(By.XPATH, xpath).text
#         if btn_name == name:
#             # context.driver.find_element(By.XPATH, xpath).click()
#             btn = context.driver.find_element(By.XPATH, xpath)
#             btn.click()
#             assert True
#     except:
#         assert False


@when(u'Open page Url: "{url}"')
def open_url(context, url):
    try:
        context.driver.get(url)
    except:
        assert False
    assert True


@when(u'Check redirect to (enter first url part) Url: "{url}"')
def check_redirect_url(context, url):
    sleep(2)
    try:
        current_url = context.driver.current_url
        if current_url.startswith(url):
            assert True
    except:
        assert False


@when(u'Find text on page Text: "{text}" element By ID: "{elem_id}"')
def find_text_id(context, text, elem_id):
    try:
        if text == context.driver.find_element(By.ID, elem_id).text:
            assert True
    except:
        assert False


@when(u'Find text on page Text: "{text}" element By XPATH: "{xpath}"')
def find_text_xpath(context, text, xpath):
    try:
        if text == context.driver.find_element(By.XPATH, xpath).text:
            assert True
    except:
        assert False


@when(u'Input Text: "{text}" element By ID: "{elem_id}"')
def input_text_id(context, text, elem_id):
    try:
        context.driver.find_element(By.ID, elem_id).send_keys(text)
        assert True
    except:
        assert False


@when(u'Input Text: "{text}" element By XPATH: "{xpath}"')
def input_text_xpath(context, text, xpath):
    try:
        context.driver.find_element(By.XPATH, xpath).send_keys(text)
        assert True
    except:
        assert False

@when(u'Sleep "{sec}" sec')
def input_text_xpath(context, sec):
    try:
        sleep(int(sec))
        assert True
    except:
        assert False

######################


@when(u'Button click by element By XPATH: "{xpath}"')
def step_impl(context, xpath):
    try:
        # btn_login = context.driver.find_element(By.XPATH, xpath).text
        context.driver.find_element(By.XPATH, xpath).click()
        # btn = context.driver.find_element(By.XPATH, xpath)
        # btn.click()
        assert True
    except:
        assert False


@when(u'Button click by element By ID: "{elem_id}"')
def step_impl(context, elem_id):
    try:
        context.driver.find_element(By.ID, elem_id).click()
        assert True, 'test'
    except:
        assert False
