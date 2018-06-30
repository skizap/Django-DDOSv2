# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
import os

from Scripts.HTTP.httpFlood import HTTPFlood
from Scripts.TCP.tcpFlood import TCPFlood
from Scripts.UDP.udpFlood import UDPFlood
from Scripts.DNS.dnsFLood import DNSFlood

from Scripts.PDF.createPDF import CreatePDF



def redirect(request):
    return HttpResponseRedirect("index")

def index(request):
    return render( request , "index.html" , {})

def Http_Flood(request):

    if request.method == "POST":
        dst = request.POST["dst"]
        Attack = HTTPFlood(dst)

        if request.POST.get("startBut"):
            Attack.Main()

        if request.POST.get("stopBut"):
            with open(os.getcwd() + "/Manage/Status.txt", "r+") as file:
                file.write("0")

        return render(request, "Http_Flood.html", {})
    else:
        return render(request, "Http_Flood.html", {})


def Tcp_Flood(request):
    if request.method == "POST":
        dst = request.POST["dst"]
        dport = request.POST["dport"]
        flag = request.POST["flag"]
        count = request.POST["count"]

    return render(request,"Tcp_Flood.html" , {})

def Udp_Flood(request):
    if request.method == "POST":
        dst = request.POST["dst"]
        dport = request.POST["dport"]
        count = request.POST["count"]


    return render(request, "Udp_Flood.html", {})


def Dns_Flood(request):
    if request.method == "POST":
        dst     = request.POST["dst"]
        qname   = request.POST["qname"]
        qtype   = request.POST["qtype"]
        count   = request.POST["count"]


    return render(request,"Dns_Flood.html")


def Rapor_Olustur(request):
    if request.method == "POST":
        raporAd = request.POST["raporAd"]
        CreatePDF(raporAd)
    return render(request ,"Rapor_Olustur.html" , {})


def Saldiri_Durumu(request):
    if request.method == "POST":
       with open(os.getcwd()+"/Manage/Status.txt" ,"r+") as file:
            file.write("0")

    return render(request ,"Saldiri_Durumu.html" , {})


