# Chapter 12
# find_element_by_* is be removed...
# please read these websites for renew:
# https://selenium-python.readthedocs.io/getting-started.html
# https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.by.html
from selenium import webdriver
from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()
browser = webdriver.Firefox()
print("type(browser): " + str(type(browser)))
browser.get('https://inventwithpython.com')
try:
    #elem = browser.find_element(By.CLASS_NAME, 'cover-thumb')
    #print('Found <%s> element with that class name!' % (elem.tag_name))
    linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
    print('type(linkElem): ' + str(type(linkElem)))
    linkElem.click() # follow the "Read Online for Free" link
except:
    print('Was not able to find an element with that name.')
