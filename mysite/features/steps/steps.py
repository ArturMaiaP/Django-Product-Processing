from behave import given
from behave import then
from behave import when
from selenium.webdriver.common.by import By
import time
import requests
#from mysite.productApp.models import Rule

ADD_RULE = "/productApp/rules/new"
field = None
value = None

@given('I want to add a new rule with the field "{f}"')
def given_field(context,f):
    global field
    field = f

@given('With the value "{v}"')
def given_value(context,v):
    global value
    value = v

@when('I save the rule')
def save_rule(context):
    ctx = context.browser
    ctx.get(context.get_url(ADD_RULE))
    ctx.find_element(By.ID, "field").send_keys(field)
    ctx.find_element(By.ID, "value").send_keys(value)
    time.sleep(2)
    ctx.find_element(By.ID, "submit-rule").click()
    time.sleep(3)


#implementar assert
@then('I should see the rule registered on the database')
def get_rules(context):
    assert True

#implementar assert
@then('The system should return the message: "{message}"')
def process_products(context,message):
    assert True
