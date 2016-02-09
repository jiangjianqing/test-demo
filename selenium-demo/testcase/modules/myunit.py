#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from driver import Browser

import unittest
import os

class MyTest(unittest.TestCase):
	def setUp(self):
		self.driver=Browser()
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()

	def tearDown(self):
		self.driver.quit()