from abc import ABCMeta, abstractmethod, ABC, abstractproperty
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtCore import Qt

import gettext
_ = gettext.gettext

class Meta(type(QTableWidget), type(ABC)):
	pass

class AutoTable(QTableWidget, metaclass=Meta):
	@abstractmethod
	def addRow(self):
		pass

	@abstractproperty
	def inflater(self):
		pass

	def inflate(self):
		self.setColumnCount(len(self.inflater))
		self.setHorizontalHeaderLabels([item['title'] for item in self.inflater])

		for index, width in enumerate([item['width'] for item in self.inflater]):
			self.setColumnWidth(index, width)

		self.horizontalHeader().setStretchLastSection(True)

	def __init__ (self):
		super().__init__()
		self.inflate()
		self.autoAddRow = True
		# Table start with 2 rows
		self.addRow()
		self.addRow()
		# Hook up the signal
		self.currentCellChanged.connect(lambda cRow, cCol, pRow, pCol: self.extendTable(cRow))

	def disableAutoAddRow(self):
		self.autoAddRow = False

	def enableAutoAddRow(self):
		self.autoAddRow = True

	def extendTable(self, currRow):
		maxRow = self.rowCount()
		if maxRow == currRow + 1 and self.autoAddRow:
			self.addRow()

	def clearEmptyRows(self):
		row = 0

		self.disableAutoAddRow()
		while row < self.rowCount():
			for col in range(self.columnCount()):
				if not self.cellWidget(row, col).isEmpty():
					break
			else:
				self.removeRow(row)
				continue
			row += 1

		if row == 0:
			self.addRow()

		self.enableAutoAddRow()

	def validateTable(self):
		valid = True

		for row in range(self.rowCount()):
			allEmpty = True
			allValid = True

			for col in range(self.columnCount):
				cell = self.cellWidget(row, col)
				allValid &= cell.valid
				allEmpty &= cell.isEmpty()

			# An empty row is skipped when parsing
			# A valid row can be parsed
			# A row that's not valid yet not empty is missing data
			# It's the table implementation to ensure that these fields make sense, e.g an empty row can't be valid
			if not allValid and not allEmpty:
				valid = False

		return valid