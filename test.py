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


# Неверные данные для авторизации
def test_BadLogin():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.zaycev.net/")

    # поиск и нажатие кнопки Войти
    driver.find_element(By.CLASS_NAME, 'wfuhyz-10.caCXzL').click()
    time.sleep(5)

    # поиск и заполнение поля EMail
    driver.find_element(By.NAME, 'login').send_keys('admin')
    # поиск и заполнение поля Password
    driver.find_element(By.NAME, 'password').send_keys('admin')
    # поиск и нажатие кнопки авторизации
    driver.find_element(By.CLASS_NAME, 'c4ymd0-0.jBhElb').click()
    time.sleep(5)

    # найти сообщение об ошибке
    error = driver.find_element(By.CLASS_NAME, 'ji2meo-3.hjwAMT')

    if error != None:
        print(error.text)
        print("Тест пройден.")
        
    assert error != None

# Тест включения музыки
def test_PlayMusic():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.zaycev.net/")

    # включить "мой плейлист дня"
    driver.find_element(By.CLASS_NAME, 'sc-11rm9om-0.hrUxqW').click()
    time.sleep(10)
    # найти кнопку паузы
    driver.find_element(By.CSS_SELECTOR, '[data-qa="player-pause"]').click()

    # найти кнопку плэй
    play_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="player-play"]')

    if play_btn != None:
        print("Тест пройден.")

    assert play_btn != None

# Тест на соответствие результатов поиска
def test_Search():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.zaycev.net/")
    
    search_text = 'abc'

    driver.find_element(By.CSS_SELECTOR, '[data-qa="header-search"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-qa="header-search"]').send_keys(search_text)
    driver.find_element(By.CSS_SELECTOR, '[data-qa="header-search-submit"]').click()

    time.sleep(5)

    track_list = driver.find_element(By.CLASS_NAME, 'bm5dwu-0.hJYea').find_elements(By.CSS_SELECTOR, '[data-qa="track"]')

    passed = True

    for track in track_list:
        if search_text not in track.get_attribute('title').lower():
            print('В треке ' + track.get_attribute('title') + ' отсутствует ' + search_text)
            passed = False

    if passed:
        print("Тест пройден.")

    assert passed
test_Search()
