# -*- coding: utf-8 -*-

class HTTPFlood():
	def __init__(self,dst,port,flag,method,count):
		self.dst	 = dst
		self.port	 = 80
		self.method  = method
		self.count	 = count