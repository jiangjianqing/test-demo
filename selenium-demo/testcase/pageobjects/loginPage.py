#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys,os
#用这种方式也可以导入库，可运行，但是在pycharm中无法识别，
#sys.path.append("..")
from time import sleep
from testcase.modules.basepage import Page
from testcase.modules.driver import Browser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class Login(Page):
	'''
	login page
	'''

	url='/'

	login_button_loc=(By.CSS_SELECTOR,"form input[type=submit]")
	login_username_loc=(By.NAME,"username")
	login_password_loc=(By.NAME,"password")

	def set_username(self,username):
		self.find_element(*self.login_username_loc).send_keys(username)

	def set_password(self,password):
		self.find_element(*self.login_password_loc).send_keys(password)

	def do_login(self):
		self.find_element(*self.login_button_loc).click()

	def user_login(self,username="admin",password="12345"):
		""" 统一登录入口
		:param username:
		:param password:
		:return:
		"""
		self.open()
		self.set_username(username)
		self.set_password(password)
		sleep(1)
		self.do_login()
		sleep(2)

if __name__=='__main__':
	print 'abs:', os.path.abspath(sys.argv[0])
	driver=Browser()
	login=Login(driver)
	login.user_login()
	driver.quit()
	#login.open()
	#login.set_username("abcdefsdf")
	#login.set_password("ttttt")
	#login.do_login()


