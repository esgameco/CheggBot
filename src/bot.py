from selenium import webdriver

class CheggBot:
    def __init__(self, profile=None, driver=None):
        self.profile = profile or webdriver.FirefoxProfile('profile')
        self.driver = driver or webdriver.Firefox(profile)