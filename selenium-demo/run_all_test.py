#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')	#解决HTMLTestRunner异常：UnicodeDecodeError: 'ascii' codec can't decode byte。。。
import os
import unittest
import time
import HTMLTestRunner
from testcase.modules import function

class AbcClass:

	def __init__(self,report_path="./report",report_title="xxx自动化测试报告",report_description='环境：linux    浏览器：firefox'):
		self.report_path=report_path
		self.report_title=report_title
		self.report_description=report_description

	#查找测试报告目录，找到最新生成的测试报告文件
	def lastest_report_filename(self):
		lists=os.listdir(self.report_path)
		lists.sort(key=lambda fn:os.path.getmtime(self.report_path+"/"+fn))
		file_new=os.path.join(self.report_path,lists[-1])
		#print(file_new)
		return file_new

	#生成新的report文件名
	def generate_new_report_filename(self):
		if not os.path.exists(self.report_path):
			os.mkdir(self.report_path)

		now=time.strftime("%Y-%m-%d %H_%M_%S")
		filename=self.report_path+"/"+now+"_report.html"
		return filename

	def execute_all_test(self):
		filename=self.generate_new_report_filename()
		fp=open(filename,'wb')
		runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=self.report_title,description=self.report_description)
		discover=unittest.defaultTestLoader.discover(start_dir="./testcase",pattern='*_sta.py')
		runner.run(discover)
		fp.close()
		return filename



if __name__=="__main__":
	report_path="./report"
	test_all=AbcClass(report_path=report_path,report_title="xx平台 自动化测试报告",report_description="环境：linux    浏览器：firefox")
	#执行所有测试，必要时可以屏蔽
	filename=test_all.execute_all_test()
	#filename=test_all.lastest_report_filename()
	print("report file="+filename)
	#用csv保存email配置
	#function.send_mail(filename,'./data/email_param.csv',title="xx平台 自动化测试报告"+"20160209")
	#用xml保存email配置
	function.send_mail(filename,'./data/email_config.xml',title="xx平台 自动化测试报告"+"20160209")
