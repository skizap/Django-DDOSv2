# -*- coding: utf-8 -*-
import os
import time
import requests
from threading import Thread
from time import gmtime , strftime
from HTTPAttackProcess import HTTP
import subprocess


ALLSTATUS = False
BANDWIDTHSIZE = []
TIME = []
PDFFlag = True

class Bandwidth():
	def __init__(self , interface):
		self.path = "/sys/class/net/{}/statistics/tx_bytes".format(interface)
		self.BandwitdArray = []
		print "Bandwith"

	def Read(self):
		while True:
			if ALLSTATUS:
				self.BandwitdArray.reverse()
				print self.BandwitdArray
				for i in range(len(self.BandwitdArray )-1):
					tmpBand = (self.BandwitdArray[i]-self.BandwitdArray[i+1]) / 128.0
					BANDWIDTHSIZE.append(tmpBand)
				break
			else:
				with open(self.path , "r") as file:
					tmp = file.read()
				self.BandwitdArray.append(int(tmp) / 1024)

				time.sleep(1.5)

class Alive():
	@staticmethod
	def isAlive():
		#./DOSS kısmı yolunu alır
		path = os.getcwd()
		with open(path+"/results.txt" , "a+") as result:
			tmp = result.readlines()

		status = ""
		for i in tmp:
			status+=(i[-4])
		os.remove(path+"/results.txt")
		os.remove(path+"/isitup_results.txt")
		return status



class HTTPFlood():
	def __init__(self,dst):
		self.targetUrl	 = dst
		self.path = os.path.dirname(__file__).rsplit("/Scripts/HTTP")[0]
		self.BashPath = os.path.dirname(__file__)

	def ReadStatusFile(self):
		global ALLSTATUS
		global TIME
		global PDFFlag

		TIME.append(self.ReturnTime())

		self.p1 = HTTP(self.targetUrl)
		self.p1.Attack()


		while True:
			time.sleep(5)
			with open(self.path+"/Status.txt" ,"r+") as file:
				tmp = file.read()

				if tmp == "1":
					print "Status.txt -> 1 <- Saldırı devam ediyor"

				if tmp == "0":
					print "Status.txt -> 0 <- Saldırı durduruldu"
					ALLSTATUS = True
					self.p1.Terminate()

					file.seek(0)
					file.write("1")
					break

		TIME.append(self.ReturnTime())
		self.WritePDFContent()

	def WritePDFContent(self):
		#PDF Content'de saldırı sonuçlarını yazma
		with open(self.path+"/PDFContent.txt" , "a+") as file:
			file.write("HTTP Flood\n")
			file.write("Baslama Zamani : {}\n".format( str(TIME[0]) ))
			file.write("Bitis Zamani : {}\n".format( str(TIME[1]) ))
			time.sleep(2)
			file.write("Status Code : {}\n".format( Alive.isAlive() ))
			file.write("Bandwith : {}\n".format( str(max(BANDWIDTHSIZE))[:5] ))
			file.write("\n")

	def ReturnTime(self):
		#Şimdiki Zamanı geriye döndürme
		return strftime("%y-%m-%d %H:%M:%S", gmtime())

	def Main(self):
		global ALLSTATUS , BANDWIDTHSIZE , TIME , PDFFlag
		ALLSTATUS = False
		BANDWIDTHSIZE = []
		TIME = []

		band = Bandwidth("wlp3s0f0")

		self.t1 = Thread(target=self.ReadStatusFile)
		self.t2 = Thread(target=band.Read)

		self.t1.start()
		self.t2.start()
