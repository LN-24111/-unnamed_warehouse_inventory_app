from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot
import gettext

_ = gettext.gettext
class Table(QTableWidget):
	def __init__(self, viewController, inflater):
		'''Hook the table with its inflater'''
		super().__init__()
		self.inflater = inflater
		self.setColumnCount(inflater.getColumnCount())
		self.setHorizontalHeaderLabels(inflater.getTitles())

		for index, width in enumerate(inflater.getWidths()):
			self.setColumnWidth(index, width)

		self.horizontalHeader().setStretchLastSection(True)
		self.columnLabels = inflater.getTitles()

		'''Sanitize user input'''
		self.itemChanged.connect(self.userInputSlot)
		self.enableInputCheck()

		self.inflater.setTable(self, viewController)
		self.viewController = viewController
		self.data = viewController.getDatas()

	@pyqtSlot(QTableWidgetItem)
	def userInputSlot(self, item):
		if not self.inputCheck:
			return
		
		self.disableInputCheck()

		self.inflater.processInput(item)

		# text = item.text().strip()
		# parser = self.inflater.getParsers()[item.column()]

		# if parser.check(text):
		# 	item.setText(parser.parse(text))
		# 	item.setBackground(Qt.white)
		# else:
		# 	item.setText(text)
		# 	item.setBackground(Qt.red)

		self.enableInputCheck()

	def addLine(self, amount):
		current = self.rowCount()
		self.setRowCount(current + amount)

		self.disableInputCheck()
		for i in range(current, current + amount):
			for j in range(self.inflater.getColumnCount()):
				item = QTableWidgetItem()
				item.setTextAlignment(self.inflater.getAlignments()[j])
				if not self.inflater.getActiveStates()[j]:
					item.editable = False
					item.setFlags(item.flags() ^ Qt.ItemIsEditable)
					item.setBackground(Qt.gray)
				else:
					item.editable = True

				self.setItem(i, j, item)

		self.setCurrentItem(self.item(current, 0))
		self.enableInputCheck()

	@pyqtSlot()
	def deleteSlot(self):
		lst = set()
		for i in self.selectedIndexes():
			lst.add(i.row())

		j = 0
		for i in lst:
			self.inflater.deleteRow(i - j)
			self.removeRow(i - j)
			j += 1

	def disableInputCheck(self):
		self.inputCheck = False

	def enableInputCheck(self):
		self.inputCheck = True

	# External control
	@pyqtSlot()
	def submitSlot(self):
		pass