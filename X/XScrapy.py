from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from Creds import USERNAME,PASSWORD

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


def login_x(username, password):
    driver.get("https://x.com/i/flow/login")
    time.sleep(5)  

    username_field = driver.find_element(By.NAME, "text")
    username_field.send_keys(username)
    username_field.send_keys(Keys.RETURN)
    time.sleep(2)  

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(2)

def acessar_url_especifica(url):
    driver.get(url)
    time.sleep(2)

username = USERNAME
password = PASSWORD

login_x(username, password)
acessar_url_especifica("https://twitter.com/usuario_exemplo")  

print(driver.title)

driver.quit()
