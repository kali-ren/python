#!/usr/bin/python
# -*- conding: utf8 -*-

import xlwt
import random

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


	def run(self,packet):
		field2 = random.randint(0,9)
		field3 = random.randint(0,9)
		field4 = random.randint(0,9)
		field5 = random.randint(0,9)
		field6 = random.randint(0,9)
		field7 = random.randint(0,9)
		field8 = random.randint(0,9)
		field9 = random.randint(0,9)
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
		queue_t = 0			# Total Queue Time
		system_t = 0		# Total System Time
		free_t = 0			# Total free time

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
