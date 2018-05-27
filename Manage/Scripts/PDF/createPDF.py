# -*- coding: utf-8 -*-

from fpdf import FPDF
import datetime
import os.path , sys
Path    = ""
Header  = ""
class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, Header)
        # Line break
        self.ln(20)
        #Logo
        self.image(Path+'/PDF/bga.png', 10, 8, 33)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def CreatePDF(header,data):
    #Burada bga.png yolu bulunamıyordu aşağıdaki 2 satır bunun çözümü
    global Path
    global Header
    """
        Header bilgisi Saldırıdan saldırıya değişiyor.Bu yüzden header createPDF'i çağıran
        kişi tarafında alınıyor.Data bilgisi ise saldırıdan sonra hedef ayakta ise ona göre
        hedef ayakta yada değil bilgisi veriyor bu bilgide CreatePDF class'ını çağıram tarafından
        veriliyor
    """
    Header = header
    Current = os.path.dirname(__file__)
    Path = os.path.abspath(os.path.join(Current, os.pardir))

    time = datetime.datetime.now()
    tmp = str(time.year) + "." + str(time.month) + "." + str(time.day)+" "+Header+".pdf"

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    for i in range(1):
        pdf.cell(0, 10, str(data))
    pdf.output(tmp, 'F')