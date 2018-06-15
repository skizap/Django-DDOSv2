# -*- coding: utf-8 -*-
import os
import time
import requests
from threading import Thread
from time import gmtime , strftime
from HTTPAttackProcess import HTTP


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
	def __init__(self,dst):
		self.orginal = dst
		self.url = dst.replace("https://","").replace("http://","").replace("www.","").replace("/","")
		self.ask = "https://isitup.org/{}".format(self.url)
		print self.ask

	def isAlive(self):
		while True and not ALLSTATUS:
			try:
				time.sleep(10)
				resp = requests.get(self.ask).text

				if "is up." in resp:
					print "Site Up"

				if "seems to be down!" in resp:
					print "Site Down"

			except:
				print "ISUP'dan veri alırken urllib fonksiyonunda hata HATAA"

class HTTPFlood():
	def __init__(self,dst):
		self.targetUrl	 = dst
		self.path = os.path.dirname(__file__).rsplit("/Scripts/HTTP")[0]

	def ReadStatusFile(self):
		global ALLSTATUS
		global TIME
		global PDFFlag

		TIME.append(self.ReturnTime())

		while True:
			time.sleep(5)
			with open(self.path+"/Status.txt" ,"r+") as file:
				tmp = file.read()

				if tmp == "1":
					print "Status.txt -> 1 <- Saldırı devam ediyor"

				if tmp == "0":
					print "Status.txt -> 0 <- Saldırı durduruldu"
					ALLSTATUS = True
					file.seek(0)
					file.write("1")
					break


		TIME.append(self.ReturnTime())

	def WritePDFContent(self):
		#PDF Content'de saldırı sonuçlarını yazma
		with open(self.path+"/PDFContent.txt" , "a+") as file:
			file.write("HTTP Flood\n")
			file.write("Baslama Zamani : {}\n".format( str(TIME[0]) ))
			file.write("Bitis Zamani : {}\n".format( str(TIME[1]) ))
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
		PDFFlag = True


		print self.targetUrl

		band  = Bandwidth("wlp3s0f0")
		alive = Alive(self.targetUrl)

		t1 = Thread(target=self.ReadStatusFile)
		t2 = Thread(target=band.Read)
		t3 = Thread(target=alive.isAlive)
		p1 = HTTP(self.targetUrl)

		t1.start()
		t2.start()
		t3.start()
		p1.Attack()

		t1.join()
		t2.join()
		t3.join()
		p1.Terminate()


		if PDFFlag:
			self.WritePDFContent()


