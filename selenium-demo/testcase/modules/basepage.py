#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Page(object):
	'''
	页面基础类
	'''

	bbs_url='http://localhost:8181/webui.springdm.springsecurity'

	def __init__(self,selenium_driver,base_url=bbs_url,parent=None):
		self.base_url=base_url
		self.driver=selenium_driver
		self.timeout=30
		self.parent=parent

	def _open(self,url):
		url=self.base_url+url
		self.driver.get(url)
		#assert self.is_on_page(),'Did not load on %s' % url

	def find_element(self,*loc):
		return self.driver.find_element(*loc)

	def find_elements(self,*loc):
		return self.driver.find_elements(*loc)

	def open(self):
		self._open(self.url)

	def is_on_page(self):
		return self.driver.current_url==(self.base_url+self.url)

	def execute_script(self,script):
		return self.driver.execute_script(script)
