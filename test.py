from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

USERNAME = open("userdata.txt").readlines()[0]
PASSWORD = open("userdata.txt").readlines()[1]

# Тест авторизации
def test_Login():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.zaycev.net/")

    # поиск и нажатие кнопки Войти
    driver.find_element(By.CLASS_NAME, 'wfuhyz-10.caCXzL').click()
    time.sleep(5)

    # поиск и заполнение поля EMail
    driver.find_element(By.NAME, 'login').send_keys(USERNAME)
    # поиск и заполнение поля Password
    driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
    # поиск и нажатие кнопки авторизации
    driver.find_element(By.CLASS_NAME, 'c4ymd0-0.jBhElb').click()
    time.sleep(5)

    # поиск кнопки аккаунта
    account_btn = driver.find_element(By.CLASS_NAME, 'wfuhyz-13')

    if account_btn != None:
        print("Авторизация пройдена.")

    assert account_btn != None


test_Login()