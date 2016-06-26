#!/usr/bin/python
# -*- conding: utf8 -*-

import xlwt, math
import random
lista=[0]
lista2=[0]
class Simula:

	def __init__(self):
		self.workbook = None
		self.sheet = None
		self.sheetName = None
		self.header = None
		self.rvg1 = None
		self.rvg2 = None
		self.table = None
		
	def setup(self, header, rvg1, rvg2, sheetName):		
		self.workbook = xlwt.Workbook()
		self.sheet = self.workbook.add_sheet(sheetName, cell_overwrite_ok=True)
		self.sheetName = sheetName
		self.header = header
		self.rvg1 = rvg1
		self.rvg2 = rvg2
		self.table = []

		self._writeHeader()

	def _writeHeader(self):
		""" Writes the Header for the Result table
		"""
		style = xlwt.XFStyle()

		# font
		font = xlwt.Font()
		font.bold = True
		style.font = font

		for i, field in enumerate(self.header):
			self.sheet.write(0, i, field, style=style)

	def vgaa(self):#vga para item a com inversa exponencial
		u = random.uniform(0,1)
		r = -12  *(math.log(1-u))#12 = media
		if r < 1:
			while r < 1:
				u = random.uniform(0,1)
				r = -12  *(math.log(u))	
		return r

	def normal(self): #vga para item b com metodo de rejeicao
		dp=1 #desvio
		x=10 #microsegundos
		u = random.uniform(0,1)
		x = -1 * math.log(u)
		u2 = random.uniform(0,1)
		e = math.exp(-(x-1)**2)/2#The method exp() returns exponential of x: e^x.
		if u2 > e:
			while u2 > e:
				u = random.uniform(0,1)
				x = math.log(u)
				u2 = random.uniform(0,1)
				e = math.exp((-(x-1)**2)/2)

		u3=random.uniform(0,1)
		if u3 > 0.5:
			return abs(u + dp*x)
		else:
			return abs(u - dp*x)

	def run(self,packet):
		field2 = self.vgaa()
		global lista
		global lista2	
		lista.append(field2+lista[packet-1])
		field3 = field2 + lista[packet-1]
		field4 = self.normal()
		field5 = self.vgaa() 	
		field6 = abs(field5-field4)
		field7 = field4+field5
		lista2.append(field7)
		field8 = field4+field6
		field9 = abs(field5 - lista2[packet-1]) 
		
		row = (packet,
			   field2, 
			   field3,
			   field4,
			   field5,
			   field6,
			   field7,
			   field8,
			   field9)

		self.table.append(row)
	
	def finish(self):
		for i, row in enumerate(self.table):
			for j, field in enumerate(row):
				self.sheet.write(i+1, j, field)
		
		style = xlwt.XFStyle()
		service_t = 0 		# Total Service Time
		queue_t = 0		# Total Queue Time
		system_t = 0		# Total System Time
		free_t = 0		# Total free time

		for row in self.table:
			service_t += row[3]
			queue_t += row[5]
			system_t += row[7]
			free_t += row[8]

		nrows = len(self.table)+1
		self.sheet.write(nrows, 3, service_t, style=style)
		self.sheet.write(nrows, 5, queue_t, style=style)
		self.sheet.write(nrows, 7, system_t, style=style)
		self.sheet.write(nrows, 8, free_t, style=style)
		
		self.workbook.save("vdc.xls")
def main():
	simulator = Simula()
	fields = ["Num Pacote", "Tempo desde\n ultima chegada", "Tempo chegada\n no relogio",
				"Tempo de servico", "Tempo inicio\n servico", "Tempo do pacote\n na fila",
				"Tempo final do\n servico no relogio", "Tempo Total no servico",
				"Tempo livre do servidor"]
	simulator.setup(fields,10,2,"proxeneta")
	for packet in range(1, 21):
		simulator.run(packet)

	simulator.finish()
if __name__ == "__main__":
	main()
