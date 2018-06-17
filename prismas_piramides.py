# -*- coding: utf-8 -*-
#Repasando pyqt like a dumbass :pp

import sys
import os
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *

clase= uic.loadUiType("prismas_piramides.ui")[0]

class Prismas_Piramides(QtGui.QMainWindow, clase):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		self.btn_calcupri.clicked.connect(self.calcula_prisma)
		self.btn_calcupiramid.clicked.connect(self.calcula_piramide)

#Inicia los calculos para prismas
	def calcula_prisma(self):		
		if self.rad_areapri.isChecked()==False and self.rad_volupri.isChecked()==False:
			print("No ha seleccionado ningún cálculo de prisma\n")
		else:
			os.system('cls')
			if self.rad_volupri.isChecked():
				print("Calculando volúmenes de prismas:=============\n")				
				self.calculavolu_circ(self.ln_rad_pri.text(), self.ln_h_pri.text())				
				self.calculavolu_rect(self.ln_bsa_pri.text(), self.ln_bsb_pri.text(), self.ln_hr_pri.text())			
				self.calculavolu_pho(self.ln_ld_pri.text(), self.ln_ap_pri.text(), self.ln_hp_pri.text())				
				
			elif self.rad_areapri.isChecked():
				print("Calculando áreas de prismas:=================\n")				
				self.calcularea_circ(self.ln_rad_pri.text(), self.ln_h_pri.text())				
				self.calcularea_rect(self.ln_bsa_pri.text(), self.ln_bsa_pri.text(), self.ln_hr_pri.text())				
				self.calcularea_pho(self.ln_ld_pri.text(), self.ln_ap_pri.text(), self.ln_hp_pri.text())				
		print("=== F I N ===\n")

#Inicia los calculos para piramides
	def calcula_piramide(self):
		if self.rad_areapira.isChecked()==False and self.rad_volupira.isChecked()==False:
			print("No ha seleccionado nungún cálculo de piramide\n")
		else:
			os.system('cls')
			if self.rad_volupira.isChecked():
				print("Calculando volúmenes de piramides:===========\n")				
				self.calculapira_circ(self.ln_rad_piramid.text(), self.ln_h_piramid.text())				
				self.calculapira_rect(self.ln_bsa_piramid.text(), self.ln_bsb_piramid.text(), self.ln_hr_piramid.text())				
				self.calculapira_pho(self.ln_ld_piramid.text(), self.ln_ap_piramid.text(), self.ln_hp_piramid.text())
			elif self.rad_areapira.isChecked():
				print("Calculando áreas de piramides:===============\n")				
				self.calcularea_circ_p(self.ln_rad_piramid.text(), self.ln_h_piramid.text())				
				self.calcularea_rect_p(self.ln_bsa_piramid.text(), self.ln_bsb_piramid.text(), self.ln_hr_piramid.text())
				self.calcularea_pho_p(self.ln_ld_piramid.text(), self.ln_ap_piramid.text(), self.ln_hp_piramid.text())
		print("=== F I N ===\n")

# Cálculo para volumen de prisma circular
	def calculavolu_circ(self, r, h):		
		if r == "" or h == "":
			pass
		else:
			try:			
				radio= float(r)
				altura= float(h)
				print("Circular: ")
				print("%.2f" %(((radio**2)*3.1416)*altura))
			except Exception:
				print("Al menos uno de los valores no es un número!\n")

# Cálculo para volumen de prisma rectangular
	def calculavolu_rect(self, a, b, h):		
		if a == "" or b == "" or h == "":
			pass
		else:
			try:			
				x= float(a)
				y= float(b)
				z= float(h)
				print("Rectangulo: ")	
				print("%.2f" %(x*y*z))
			except Exception:
				print("Al menos uno de los valores no es un número!\n")		

# Cálculo para volumen de prisma poligonal
	def calculavolu_pho(self, l, ap, h):
		if l == "" or ap == "" or h == "":
			pass
		else:
			try:
				x = float(l)
				y = float(ap)
				z = float(h)
				print("Poligonal: ")
				if self.cmb_p_h_o_pri.currentText()=="Pentagonal":
					print("%.2f" %(((x*5*y)/2)*z))
				if self.cmb_p_h_o_pri.currentText()=="Hexagonal":
					print("%.2f" %(((x*6*y)/2)*z))
				if self.cmb_p_h_o_pri.currentText()=="Heptagonal":
					print("%.2f" %(((x*7*y)/2)*z))
				if self.cmb_p_h_o_pri.currentText()=="Octagonal":
					print("%.2f" %(((x*8*y)/2)*z))
			except Exception:
				print("Al menos uno de los valores no es un número!\n")

# Cálculo para area de prisma circular
	def calcularea_circ(self, r, h):		
		if r == "" or h == "":
			pass
		else:
			try:			
				radio= float(r)
				altura= float(h)
				print("Circular: ")
				print("%.2f" %(2*((radio**2)*3.1416)+(2*altura*radio)))
			except Exception:
				print("Al menos uno de los valores no es un número!\n")

# Cálculo para area de prisma rectangular
	def calcularea_rect(self, a, b, h):		
		if a == "" or b == "" or h == "":
			pass
		else:
			try:			
				x= float(a)
				y= float(b)
				z= float(h)
				print("Rectangular: ")				
				print("%.2f" %(2*x*y + 2*z*(x+y)))
			except Exception:
				print("Al menos uno de los valores no es un número!\n")	

# Cálculo para area de prisma poligonal
	def calcularea_pho(self, l, ap, h):
		if l == "" or ap == "" or h == "":
			pass
		else:
			try:
				x = float(l)
				y = float(ap)
				z = float(h)
				print("Poligonal: ")
				if self.cmb_p_h_o_pri.currentText()=="Pentagonal":
					print("%.2f" % (2*((x*5*y)/2) + 5*(z*x)))
				if self.cmb_p_h_o_pri.currentText()=="Hexagonal":
					print("%.2f" % (2*((x*6*y)/2) + 6*(z*x)))
				if self.cmb_p_h_o_pri.currentText()=="Heptagonal":
					print("%.2f" % (2*((x*7*y)/2) + 7*(z*x)))
				if self.cmb_p_h_o_pri.currentText()=="Octagonal":
					print("%.2f" % (2*((x*8*y)/2) + 8*(z*x)))
			except Exception:
				print("Al menos uno de los valores no es un número!\n")

# Cálculo para volumen de piramide circular
	def calculapira_circ(self, r, h):
		if r == "" or h == "":
			pass
		else:
			try:
				radio= float(r)
				altura= float(h)
				print("Circular: ")
				print("%.2f" %(((3.1416*(radio**2))*altura)/3))
			except Exception:
				print("Al menos uno de los valores no es un número!\n")

# Cálculo para volumen de piramide rectangular
	def calculapira_rect(self, a, b, h):
		if a == "" or b == "" or h == "":
			pass
		else:
			try:			
				x= float(a)
				y= float(b)
				z= float(h)
				print("Rectangular: ")			
				print("%.2f" %((x*y*z)/3))
			except Exception:
				print("Al menos uno de los valores no es un número!\n")	

# Cálculo para volumen de piramide poligonal
	def calculapira_pho(self, l, ap, h):
		if l == "" or ap == "" or h == "":
			pass
		else:
			try:
				x = float(l)
				y = float(ap)
				z = float(h)
				print("Poligonal: ")
				if self.cmb_p_h_o_piramid.currentText()=="Pentagonal":
					print("%.2f" %((((x*5*y)/2)*z)/3))
				if self.cmb_p_h_o_piramid.currentText()=="Hexagonal":
					print("%.2f" %((((x*6*y)/2)*z)/3))
				if self.cmb_p_h_o_piramid.currentText()=="Heptagonal":
					print("%.2f" %((((x*7*y)/2)*z)/3))
				if self.cmb_p_h_o_piramid.currentText()=="Octagonal":
					print("%.2f" %((((x*8*y)/2)*z)/3))
			except Exception:
				print("Al menos uno de los valores no es un número!\n")

# Cálculo para area de piramide circular
	def calcularea_circ_p(self, r, h):
		if r == "" or h == "":
			pass
		else:
			try:
				radio= float(r)
				altura= float(h)
				apot_lat= float(((radio**2)+(altura**2))**.5)
				print("Circular: ")
				print("%.2f" % ((3.1416*radio)*(radio+apot_lat)))
			except ValueError:
				print("Al menos uno de los valores no es un número!\n")

# Cálculo para area de piramide rectangular
	def calcularea_rect_p(self, a, b, h):
		if a == "" or b == "" or h == "":
			pass
		else:
			try:
				x= float(a)
				y= float(b)
				z= float(h)
				print("Poligonal: ")
				sqrtx= float(((z**2) + (x**2)/4)**.5)
				sqrty= float(((z**2) + (y**2)/4)**.5)
				print("Rectangular: ")
				print("%.2f" % (x*y + y*sqrtx + x*sqrty))
			except ValueError:
				print("Al menos uno de los valores no es un número!\n")

# Cálculo para area de piramide poligonal
	def calcularea_pho_p(self, l, ap, h):
		if l == "" or ap == "" or h == "":
			pass
		else:
			try:
				x= float(l)
				y= float(ap)
				z= float(h)
				print("Poligonal: ")
				apot_lat= float(((z**2)+(y**2))**.5)
				if self.cmb_p_h_o_piramid.currentText()=="Pentagonal":
					print("%.2f" % (((5*x)/2)*(y+apot_lat)))
				if self.cmb_p_h_o_piramid.currentText()=="Hexagonal":
					print("%.2f" % (((6*x)/2)*(y+apot_lat)))
				if self.cmb_p_h_o_piramid.currentText()=="Heptagonal":
					print("%.2f" % (((7*x)/2)*(y+apot_lat)))
				if self.cmb_p_h_o_piramid.currentText()=="Octagonal":
					print("%.2f" % (((8*x)/2)*(y+apot_lat)))
			except ValueError:
				print("Al menos uno de los valores no es un número!\n")
		
app= QtGui.QApplication(sys.argv)
Ventana= Prismas_Piramides()
Ventana.show()
print("Versión 1.0, limitantes:")
print("* Limitación a 3 caracteres en inputs")
print("* Resultados mostrados en consola; cada nueva orden borra la pantalla")
print("* TODO ES EN BASE A FIGURAS REGULARES")
app.exec_()