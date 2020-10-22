from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.server_url = 'http://localhost:8000'



