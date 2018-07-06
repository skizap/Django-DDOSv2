# -*- coding: utf-8 -*-

from fpdf import FPDF
import datetime
import os.path  , sys
import random
import numpy as np
import matplotlib.pyplot as plt


Header  = ""
class PDF(FPDF):
    def header(self):
        self.Path = os.path.dirname(__file__)

        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, Header)
        # Line break
        self.ln(20)
        #Logo
        self.image(self.Path+'/bga.png', 10, 8, 33)

    def addImage(self , name):
        self.image(os.getcwd()+"/"+name+".png" , 10,100,100 )

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def CreateGraph(name,arr):
    #data = ['0', '0', 2, '0', '0', '0', '0', '0', '0', '0', '0']
    data = arr
    xs = np.repeat(range(len(data)), 2)
    ys = np.repeat(data, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.plot(xs, ys)
    plt.ylim(-0.5, 3)
    plt.suptitle(name, fontsize=16)
    plt.xlabel('TIME')
    plt.ylabel('STATUS')
    plt.savefig(name, dpi=100)


def CreatePDF(Name):
    GrapName = ""

    time = datetime.datetime.now()

    tmp = str(time.year) + "." + str(time.month) + "." + str(time.day)+" "+Name+".pdf"
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)


    path = os.path.dirname(__file__).rsplit("/Scripts/PDF")[0]
    with open(path+"/PDFContent.txt" ,"r+") as file:
        arr = file.readlines()

    for i in arr:
        if not ":" in i:
            GrapName = i

        if i.startswith("Status"):
            GrapArr = list(i.split(":")[1].lstrip().split("\n")[0])
            print GrapArr
            CreateGraph(GrapName.split()[0] , GrapArr)
            pdf.addImage(GrapName.split()[0])
        else:
            pdf.multi_cell(0, 10, i, 0, 1)
            pdf.ln(5)



    pdf.output(tmp, 'F')
