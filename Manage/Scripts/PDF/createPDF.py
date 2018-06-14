# -*- coding: utf-8 -*-

from fpdf import FPDF
import datetime
import os.path , sys
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

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def CreatePDF(Name):

    time = datetime.datetime.now()
    tmp = str(time.year) + "." + str(time.month) + "." + str(time.day)+" "+Name+".pdf"
    arr = []
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)


    path = os.path.dirname(__file__).rsplit("/Scripts/PDF")[0]
    with open(path+"/PDFContent.txt" ,"r+") as file:
        arr = file.readlines()

    for i in arr:
        pdf.multi_cell(0, 10, i, 0, 1)
        pdf.ln(5)
    pdf.output(Name, 'F')
