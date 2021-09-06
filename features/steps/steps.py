from behave import *
from selenium.webdriver.common.by import By
from resources.page_objects import PageObjects
from data import labels
import time

use_step_matcher=("parse")


@given(u'I am on the CICOD Page')
def step_impl(context):
    context.driver = PageObjects()
    context.driver.launch_browser(labels.url)


@when(u'I click on "{text}"')
def step_impl(context, text):
    if text == "SignUp":
        context.driver.page_load(By.CSS_SELECTOR, labels.start_trial)
        context.driver.click_an_element(By.CSS_SELECTOR, labels.start_trial)
    elif text == "Next":
        context.driver.page_load(By.CSS_SELECTOR, labels.next_button)
        context.driver.click_an_element(By.CSS_SELECTOR, labels.next_button)
    elif text == "a Plan":
        context.driver.page_load(By.CSS_SELECTOR, labels.plan_page_select)
        context.driver.click_an_element(By.CSS_SELECTOR, labels.plan_page_select)
    elif text == "Next Button":
        context.driver.scroll_down()
        context.driver.page_load(By.CSS_SELECTOR, labels.plan_next)
        context.driver.click_an_element(By.CSS_SELECTOR, labels.plan_next)
    elif text == "Terms of use":
        context.driver.page_load(By.CSS_SELECTOR, labels.referral_agree)
        context.driver.click_an_element(By.CSS_SELECTOR, labels.referral_agree)
    elif text == "Start free trial":
        context.driver.page_load(By.CSS_SELECTOR, labels.referral_start_free_trial)
        context.driver.click_an_element(By.CSS_SELECTOR, labels.referral_start_free_trial)
        time.sleep(10)


@when(u'I insert the "{text}"')
def step_impl(context, text):
    if text == "Email":
        context.driver.page_load(By.CSS_SELECTOR, labels.email_trial)
        context.driver.insert_a_text(By.CSS_SELECTOR, labels.email_trial, labels.input_email)
    elif text == "phone number":
        context.driver.page_load(By.CSS_SELECTOR, labels.phone_number)
        context.driver.insert_a_text(By.CSS_SELECTOR, labels.phone_number, labels.digits_phone_number)
    elif text == "business name":
        context.driver.page_load(By.CSS_SELECTOR, labels.business_name)
        context.driver.insert_a_text(By.CSS_SELECTOR, labels.business_name, labels.input_business_name)


@step(u'I select an info from the list')
def step_impl(context):
        context.driver.page_load(By.CSS_SELECTOR, labels.info_control_panel)
        context.driver.select_an_item(By.CSS_SELECTOR, labels.info_control_panel, labels.text_display)
        time.sleep(10)

