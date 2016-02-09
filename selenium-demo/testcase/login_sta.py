#!/usr/bin/python
# -*- coding: UTF-8 -*-

from time import sleep
import random,unittest
from testcase.modules import myunit
from testcase.pageobjects.loginPage import Login
from testcase.modules import function

class loginTest(myunit.MyTest):
	''' 登录测试
	'''


	def user_login_verity(self,username="",password=""):
		Login(self.driver).user_login(username,password)

	def test_login1(self):
		'''用户名、密码为空登录'''
		self.user_login_verity()
		po=Login(self.driver)
		#self.assertEqual()
		function.snapshot_img(self.driver,"user_password_empty.png")

	def test_login2(self):
		'''用户名正确、密码为空登录'''
		self.user_login_verity(username="admin")
		self.assertEqual("密码不能为空","密码不能为空")
		function.snapshot_img(self.driver,"password_empty.png")

	def test_login3(self):
		'''用户名为空，密码正确'''
		po=Login(self.driver)
		self.assertEqual("用户名不能为空","用户名不能为空")
		self.user_login_verity(password="abc123456")

	def test_login4(self):
		'''用户名与密码不匹配'''
		character=random.choice("zyxwvutsrqponmlkjihgfedcba")
		username="zhangsan"+character
		self.user_login_verity(username=username,password="123456")
		po=Login(self.driver)
		self.assertEqual("密码与帐号不匹配","密码与帐号不匹配")
		function.snapshot_img(self.driver,"user_password_error.png")


	def test_login5(self):
		'''用户名、密码正确'''

		self.user_login_verity(username="admin12312",password="123456_8349349349")
		#sleep(2)
		po=Login(self.driver)
		self.assertEqual("张三","张三")
		function.snapshot_img(self.driver,"user_password_true.png")


if __name__=="__main__":
	unittest.main()