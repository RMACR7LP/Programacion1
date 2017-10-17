#-*- coding: utf-8 -*-

import reportlab
from reportlab.pdfgen import canvas
c=canvas.Canvas("Prueba.pdf")
c.drawString(100,100,'hola')
c.save()
