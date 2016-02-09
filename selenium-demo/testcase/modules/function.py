#!/usr/bin/python
# -*- coding: UTF-8 -*-
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from selenium import webdriver
import os,sys

# 截图函数
def snapshot_img(driver,file_name):
	"""

	:param driver: webdriver
	:param file_name: 截图文件名，不要带后缀，默认为png
	:return:
	"""
	#print(__file__)

	#获取脚本路径
	path = sys.path[0]
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
	if os.path.isdir(path):
		base_dir= path
	elif os.path.isfile(path):
		base_dir= os.path.dirname(path)
	#base_dir=os.path.dirname(os.path.dirname(__file__))
	#print(base_dir)
	base_dir=base_dir.replace('\\','/')
	base=base_dir.split('testcase')[0]
	file_path=base+"report/image/"+file_name.split(".")[0]+".png"
	print(file_path)
	driver.get_screenshot_as_file(file_path)

def send_mail(report_html_file,title="xxxx自动化测试报告"):
	'''将html report文件发送到指定邮箱'''
	f=open(report_html_file,mode='rb')
	mail_body=f.read()
	f.close()

	msg=MIMEText(mail_body,'html','utf-8')
	msg['Subject']=Header(title,'utf-8')
	smtp=smtplib.SMTP()
	smtp.connect("smtp.263.net")
	#uiy87654
	smtp.login("jianqingjiang@focusight.net","ztxs20150326")
	smtp.sendmail("jianqingjiang@focusight.net","cz_jjq@qq.com",msg.as_string())
	smtp.quit()
	print("email has send out!")


if __name__=='__main__':
	driver=webdriver.Firefox()
	driver.get("http://www.baidu.com")
	snapshot_img(driver,'baidu.jpg')
	driver.quit()