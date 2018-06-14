# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect

from Scripts.HTTP.httpFlood import HTTPFlood
from Scripts.TCP.tcpFlood import TCPFlood
from Scripts.UDP.udpFlood import UDPFlood
from Scripts.DNS.dnsFLood import DNSFlood

from Scripts.PDF.createPDF import CreatePDF
from Scripts.LIVE.isAlive import isAlive
from Scripts.RESOLVE.DomainResolve import Resolve



def redirect(request):
    return HttpResponseRedirect("index")

def index(request):
    return render( request , "index.html" , {})

def Http_Flood(request):
    if request.method == "POST":
        dst     = request.POST["dst"]

        Attack = HTTPFlood(dst)
        Attack.Main()

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

