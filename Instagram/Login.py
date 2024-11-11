from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Creds import INSTAGRAM_LOGIN_PATH

import time

def instagram_login(driver, username, password):
    
    driver.get(INSTAGRAM_LOGIN_PATH)
    
    
    time.sleep(3)
    
    
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    
    username_input.send_keys(username)
    password_input.send_keys(password)
    
    
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    
    time.sleep(5)