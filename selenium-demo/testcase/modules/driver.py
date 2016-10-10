#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium.webdriver import Remote
#from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

def Browser(is_local=True,host='127.0.0.1:4444',browser_name='firefox'):
	if is_local==True:

		#用lambda表达式来模仿switch
		drivers = {
		  'firefox': lambda: webdriver.Chrome(),
		  'b': lambda x: x + 7,
		  'c': lambda x: x - 2
		}
		#driver=drivers.get(browser_name,lambda: webdriver.Firefox())()
		driver=drivers[browser_name]()

		#driver = webdriver.Firefox() # Get local session of firefox
	else:
		#下面为使用selenium-server时的参数
		dc={'browserName':browser_name}	# 指定浏览器('chrome','firefox')
		driver=Remote(command_executor='http://'+host+'/wd/hub',desired_capabilities=dc)
	return driver

if __name__=='__main__':
	browser=Browser()
	browser.get("http://www.yahoo.com") # Load page
	assert "Yahoo" in browser.title
	elem = browser.find_element_by_name("p") # Find the query box
	elem.send_keys("seleniumhq" + Keys.RETURN)
	time.sleep(0.2) # Let the page load, will be added to the API
	try:
			browser.find_element_by_xpath("//a[contains(@href,'http://www.seleniumhq.org')]")
	except NoSuchElementException:
			assert 0, "can't find seleniumhq"
	finally:
		#browser.close()
		browser.quit()