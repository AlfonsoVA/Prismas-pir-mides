# -*- coding: utf-8 -*-
import sys
import os
from PyQt5 import QtGui, QtCore, uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *

clase = uic.loadUiType("prismas_piramides.ui")[0]

class Prismas_Piramides(QtWidgets.QMainWindow, clase):
	def __init__(self):		
		QtWidgets.QMainWindow.__init__(self)
		self.setupUi(self)
		self.btn_calcupri.clicked.connect(self.calcula_prisma)
		self.btn_calcupiramid.clicked.connect(self.calcula_piramide)
	
	#Inicia los calculos para prismas
	def calcula_prisma(self):		
		if not(self.rad_areapri.isChecked()) or not(self.rad_volupri.isChecked()):						
			#Calculando volúmenes de prismas:=============
			if self.rad_volupri.isChecked():								
				self.calculavolu_circ(self.ln_rad_pri.text(), self.ln_h_pri.text())				
				self.calculavolu_rect(self.ln_bsa_pri.text(), self.ln_bsb_pri.text(), self.ln_hr_pri.text())			
				self.calculavolu_pho(self.ln_ld_pri.text(), self.ln_ap_pri.text(), self.ln_hp_pri.text())				

			#Calculando áreas de prismas:=================				
			elif self.rad_areapri.isChecked():				
				self.calcularea_circ(self.ln_rad_pri.text(), self.ln_h_pri.text())				
				self.calcularea_rect(self.ln_bsa_pri.text(), self.ln_bsa_pri.text(), self.ln_hr_pri.text())				
				self.calcularea_pho(self.ln_ld_pri.text(), self.ln_ap_pri.text(), self.ln_hp_pri.text())						

	#Inicia los calculos para piramides
	def calcula_piramide(self):
		if not(self.rad_areapira.isChecked()) or not(self.rad_volupira.isChecked()):						
			#Calculando volúmenes de piramides:=============
			if self.rad_volupira.isChecked():				
				self.calculapira_circ(self.ln_rad_piramid.text(), self.ln_h_piramid.text())				
				self.calculapira_rect(self.ln_bsa_piramid.text(), self.ln_bsb_piramid.text(), self.ln_hr_piramid.text())				
				self.calculapira_pho(self.ln_ld_piramid.text(), self.ln_ap_piramid.text(), self.ln_hp_piramid.text())
			#Calculando áreas de prismas:=============
			elif self.rad_areapira.isChecked():				
				self.calcularea_circ_p(self.ln_rad_piramid.text(), self.ln_h_piramid.text())				
				self.calcularea_rect_p(self.ln_bsa_piramid.text(), self.ln_bsb_piramid.text(), self.ln_hr_piramid.text())
				self.calcularea_pho_p(self.ln_ld_piramid.text(), self.ln_ap_piramid.text(), self.ln_hp_piramid.text())	

	#Cálculo para volumen de prisma circular
	def calculavolu_circ(self, r, h):		
		if r == "" or h == "":
			pass
		else:
			try:			
				radio= float(r)
				altura= float(h)				
				self.lcd_prism_cir.display(((radio**2)*3.1416)*altura)				
			except Exception:
				print("Al menos uno de los valores no es un número!\n")

	#Cálculo para volumen de prisma rectangular
	def calculavolu_rect(self, a, b, h):		
		if a == "" or b == "" or h == "":
			pass
		else:
			try:			
				x= float(a)
				y= float(b)
				z= float(h)				
				self.lcd_prism_rec.display(x*y*z)
			except Exception:
				print("Al menos uno de los valores no es un número!\n")		

	#Cálculo para volumen de prisma poligonal
	def calculavolu_pho(self, l, ap, h):
		if l == "" or ap == "" or h == "":
			pass
		else:
			try:
				x = float(l)
				y = float(ap)
				z = float(h)				
				if self.cmb_p_h_o_pri.currentText()=="Pentagonal":
					self.lcd_prism_pho.display(((x*5*y)/2)*z)					
				if self.cmb_p_h_o_pri.currentText()=="Hexagonal":
					self.lcd_prism_pho.display(((x*6*y)/2)*z)					
				if self.cmb_p_h_o_pri.currentText()=="Heptagonal":
					self.lcd_prism_pho.display(((x*7*y)/2)*z)					
				if self.cmb_p_h_o_pri.currentText()=="Octagonal":
					self.lcd_prism_pho.display(((x*8*y)/2)*z)					
			except Exception:
				print("Al menos uno de los valores no es un número!\n")

	#Cálculo para area de prisma circular
	def calcularea_circ(self, r, h):		
		if r == "" or h == "":
			pass
		else:
			try:			
				radio= float(r)
				altura= float(h)				
				self.lcd_prism_cir.display(2*((radio**2)*3.1416)+(2*altura*radio))				
			except Exception:
				print("Al menos uno de los valores no es un número!\n")

	#Cálculo para area de prisma rectangular
	def calcularea_rect(self, a, b, h):		
		if a == "" or b == "" or h == "":
			pass
		else:
			try:			
				x= float(a)
				y= float(b)
				z= float(h)
				self.lcd_prism_rec.display(2*x*y + 2*z*(x+y))				
			except Exception:
				print("Al menos uno de los valores no es un número!\n")	

	#Cálculo para area de prisma poligonal
	def calcularea_pho(self, l, ap, h):
		if l == "" or ap == "" or h == "":
			pass
		else:
			try:
				x = float(l)
				y = float(ap)
				z = float(h)				
				if self.cmb_p_h_o_pri.currentText()=="Pentagonal":
					self.lcd_prism_pho.display(2*((x*5*y)/2) + 5*(z*x))					
				if self.cmb_p_h_o_pri.currentText()=="Hexagonal":					
					self.lcd_prism_pho.display(2*((x*6*y)/2) + 6*(z*x))
				if self.cmb_p_h_o_pri.currentText()=="Heptagonal":
					self.lcd_prism_pho.display(2*((x*7*y)/2) + 7*(z*x))					
				if self.cmb_p_h_o_pri.currentText()=="Octagonal":
					self.lcd_prism_pho.display(2*((x*8*y)/2) + 8*(z*x))					
			except Exception:
				print("Al menos uno de los valores no es un número!\n")

	#Cálculo para volumen de piramide circular
	def calculapira_circ(self, r, h):
		if r == "" or h == "":
			pass
		else:
			try:
				radio= float(r)
				altura= float(h)				
				self.lcd_pir_cir.display(((3.1416*(radio**2))*altura)/3)				
			except Exception:
				print("Al menos uno de los valores no es un número!\n")
	
	#Cálculo para volumen de piramide rectangular
	def calculapira_rect(self, a, b, h):
		if a == "" or b == "" or h == "":
			pass
		else:
			try:			
				x= float(a)
				y= float(b)
				z= float(h)				
				self.lcd_pir_rec.display((x*y*z)/3)				
			except Exception:
				print("Al menos uno de los valores no es un número!\n")	

	#Cálculo para volumen de piramide poligonal
	def calculapira_pho(self, l, ap, h):
		if l == "" or ap == "" or h == "":
			pass
		else:
			try:
				x = float(l)
				y = float(ap)
				z = float(h)				
				if self.cmb_p_h_o_piramid.currentText()=="Pentagonal":
					self.lcd_pir_pho.display((((x*5*y)/2)*z)/3)					
				if self.cmb_p_h_o_piramid.currentText()=="Hexagonal":
					self.lcd_pir_pho.display((((x*6*y)/2)*z)/3)					
				if self.cmb_p_h_o_piramid.currentText()=="Heptagonal":
					self.lcd_pir_pho.display((((x*7*y)/2)*z)/3)					
				if self.cmb_p_h_o_piramid.currentText()=="Octagonal":
					self.lcd_pir_pho.display((((x*8*y)/2)*z)/3)					
			except Exception:
				print("Al menos uno de los valores no es un número!\n")

	#Cálculo para area de piramide circular
	def calcularea_circ_p(self, r, h):
		if r == "" or h == "":
			pass
		else:
			try:
				radio= float(r)
				altura= float(h)
				apot_lat= float(((radio**2)+(altura**2))**.5)				
				self.lcd_pir_cir.display((3.1416*radio)*(radio+apot_lat))				
			except ValueError:
				print("Al menos uno de los valores no es un número!\n")

	#Cálculo para area de piramide rectangular
	def calcularea_rect_p(self, a, b, h):
		if a == "" or b == "" or h == "":
			pass
		else:
			try:
				x= float(a)
				y= float(b)
				z= float(h)				
				sqrtx= float(((z**2) + (x**2)/4)**.5)
				sqrty= float(((z**2) + (y**2)/4)**.5)				
				self.lcd_pir_pho.display((x*y + y*sqrtx + x*sqrty))				
			except ValueError:
				print("Al menos uno de los valores no es un número!\n")
	
	#Calcula area de piramide poligonal 
	def calcularea_pho_p(self, l, ap, h):
		if l == "" or ap == "" or h == "":
			pass
		else:
			try:
				x= float(l)
				y= float(ap)
				z= float(h)				
				apot_lat= float(((z**2)+(y**2))**.5)
				if self.cmb_p_h_o_piramid.currentText()=="Pentagonal":
					self.lcd_pir_pho.display(((5*x)/2)*(y+apot_lat))										
				if self.cmb_p_h_o_piramid.currentText()=="Hexagonal":
					self.lcd_pir_pho.display(((6*x)/2)*(y+apot_lat))					
				if self.cmb_p_h_o_piramid.currentText()=="Heptagonal":
					self.lcd_pir_pho.display(((7*x)/2)*(y+apot_lat))					
				if self.cmb_p_h_o_piramid.currentText()=="Octagonal":
					self.lcd_pir_pho.display(((8*x)/2)*(y+apot_lat))					
			except ValueError:
				print("Al menos uno de los valores no es un número!\n")
		
app = QApplication(sys.argv)
Ventana = Prismas_Piramides()
Ventana.show()
app.exec_()