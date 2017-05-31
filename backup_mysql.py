# coding:utf8
__author__ = 'check)h'

"""
	备份mysql数据库
	利用mysqldum命令备份
	备份文件命名为执行成功时间
	保留最近两次备份文件
"""

import os
import time

class BackupMysql(object):
	def __init__(self,BackupCommond,Database,BackupDir):
		self.Bc = BackupCommond
		self.Db = Database
		self.Bdir = BackupDir

	def BackName(self):
		return str(self.Db + time.strftime('-%y%m%d-%H:%M:%S') + '.sql')   #返回带时间的文件名

	def ExistsDir(self):
		if not os.path.exists(self.Bdir):   #判断备份目录是否存在
			os.mkdir(self.Bdir)
		return self.Bdir

	def Commond(self):
		try:
		    os.popen(self.Bc + ' ' +self.Db + u' > ' + self.ExistsDir() + self.BackName())   #执行备份命令
        except Exception,e:
			return e

	def back_up(self):
		if len(os.listdir(self.ExistsDir())) == 2:  #备份目录只保留最新的二次备份
			if	os.path.getctime(self.ExistsDir()+os.listdir(self.ExistsDir())[0]) > os.path.getctime(self.ExistsDir()+os.listdir(self.ExistsDir())[1]):
				os.remove(self.ExistsDir()+os.listdir(self.ExistsDir())[1])
			else:
				os.remove(self.ExistsDir()+os.listdir(self.ExistsDir())[0])
		self.Commond()



if __name__ == '__main__':
	test = BackupMysql('/usr/bin/mysqldump -uroot -ptest ','test','/home/BackSql/sql/')
	test.back_up()