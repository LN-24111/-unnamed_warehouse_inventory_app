from PyQt5.QtCore import Qt
from controller.fieldcheck import *

def _(message): return message

# Handles customized table GUI
# Stores and processes table data
class _Inflater:
	def __init__(self):
		self.datas = []
		self.deleted = []

	# GUI
	def getTitles(self):
		return [item['title'] for item in self.columns]

	def getWidths(self):
		return [item['width'] for item in self.columns]

	def getAlignments(self):
		return [item['alignment'] for item in self.columns]

	def getActiveStates(self):
		return [item['active'] for item in self.columns]

	def getParsers(self):
		return [item['parser'] for item in self.columns]

	def getImportantKeys(self):
		return self.important

	def getColumnCount(self):
		return len(self.columns)

	# Data
	def setTable(self, table, controller):
		self.table = table
		self.controller = controller

		data = controller.getDatas()
		labels = self.getTitles()

		self.table.addRows(len(data))

		for item in data:
			self.datas.append(item)

			for i, dataline in enumerate(data):
				row = dataline.data

				for cell in row:
					if cell in self.columnLabels:
						j = self.columnLabels.index(cell)
						self.item(i, j).setText(str(row[cell]))


	def addRows(self, count):
		for i in range(count):
			self.datas.append([None])

	def deleteRow(self, row):
		self.deleted.append(self.datas[row])
		del self.datas[row]

	def submit(self):
