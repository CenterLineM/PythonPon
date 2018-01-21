# 


import http.client
from time import time
from os import isfile
from os import stat

# 先調用須用套件包
def GetUrlFileSize(URL):
	try:  
		# 列外處理
		#從URL 得host 和 文件path
		url=str(URL)
		index=url.find('/')
		if(index == -1)
			print('url is invalid,connot pare')
			return -1 
		else
			host=url[0:index]
			path=url[index:]
		print('The url is %s , host is %s, path is %s'%(URL,host,path))
		#
		conn =http.client.HTTPConnection(host)
		#
		print('Connection have be creative')
