from selenium import webdriver
from selenium_stealth import stealth
from typing import *

class CheggBot:
    def __init__(self, options=None, driver=None):
        self.options = options or webdriver.ChromeOptions()
        self.options.add_argument('start-maximized')
        # self.options.add_argument("--headless")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)

        self.driver = driver or webdriver.Chrome(options=self.options, executable_path=r"C:\Users\chanc\Documents\Projects\CheggBot\chromedriver.exe")
        stealth(
            driver = self.driver,
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
            languages = ["en-US", "en"],
            vendor = "Google Inc.",
            platform = "Win32",
            webgl_vendor = "Intel Inc.",
            renderer = "Intel Iris OpenGL Engine",
            fix_hairline = False,
            run_on_insecure_origins = False,
        )
    
    def goto(self, url):
        self.driver.get(url)