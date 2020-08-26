from selenium.webdriver.chrome.options import Options


def getChromeOptions():
    options = Options()
    options.add_argument("user-data-dir=selenium")
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-popup-blocking")
    return options
