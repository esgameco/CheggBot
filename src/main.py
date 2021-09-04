from selenium import webdriver

profile = webdriver.FirefoxProfile('profile')
driver = webdriver.Firefox()

driver.get('http://www.google.com')