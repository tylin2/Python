# Chapter 12
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://nostarch.com')
htmlElem = browser.find_element(By.TAG_NAME, 'html')
htmlElem.send_keys(Keys.END)    # scrolls to bottom
#htmlElem.send_keys(Keys.HOME)   # scrolls to top
