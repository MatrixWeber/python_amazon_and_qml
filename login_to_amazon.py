from chrome_options import getChromeOptions
from selenium import webdriver
from time import sleep


def login_to_amazon(login, password):
    driver = webdriver.Chrome('C:/Users/Alex/Downloads/chromedriver_win32/chromedriver.exe', options=getChromeOptions())

    driver.get('https://amazon.de')
    loginButton = driver.find_element_by_css_selector('#nav-signin-tooltip > a > span')
    loginButton.click()

    sleep(1)
    driver.find_element_by_css_selector('#ap_email').send_keys(login)
    continueButton = driver.find_element_by_css_selector('#continue')
    continueButton.click()

    sleep(1)
    driver.find_element_by_css_selector('#ap_password').send_keys(password)
    signInSubmitButton = driver.find_element_by_css_selector('#signInSubmit')
    signInSubmitButton.click()

    return driver