from PyQt5.Qt import pyqtSlot
from PyQt5.QtWidgets import QTableWidgetItem
from view.table.autotable import AutoTable
from view.table.edittextcell import EditTextCell

def _(msg): return msg

class NewProductTable(AutoTable):
	@property
	def inflater(self):
		return [{'title':_('PID'), 'width': 100},
				{'title':_('Name'), 'width': 140},
				{'title':_('Format'), 'width': 120},
				{'title':_('Unit'), 'width': 70},
				{'title':_('VAT'), 'width': 50},
				{'title':_('Manufacturer'), 'width': 145},
				{'title':_('Origin'), 'width': 100}]

	def __init__(self, controller, validator):
		super().__init__()
		self.controller = controller
		self.validator = validator

	def addRow(self):
		newRowIndex = self.rowCount()
		newRowCount = newRowIndex + 1
		self.setRowCount(newRowCount)

		# Declare the cells
		pidCell = EditTextCell()
		nameCell = EditTextCell()
		formatCell = EditTextCell()
		unitCell = EditTextCell()
		vatCell = EditTextCell(True) # not important
		manufacturerCell = EditTextCell()
		originCell = EditTextCell()

		# Hooking up events corresponding to specific inputs
		pidCell.newUserInput.connect(self.pidInput)
		nameCell.newUserInput.connect(self.nameInput)
		formatCell.newUserInput.connect(self.formatInput)
		unitCell.newUserInput.connect(self.unitInput)
		manufacturerCell.newUserInput.connect(self.manufacturerInput)
		originCell.newUserInput.connect(self.originInput)

		# Setting items
		self.setCellWidget(newRowIndex, 0, pidCell)
		self.setCellWidget(newRowIndex, 1, nameCell)
		self.setCellWidget(newRowIndex, 2, formatCell)
		self.setCellWidget(newRowIndex, 3, unitCell)
		self.setCellWidget(newRowIndex, 4, vatCell)
		self.setCellWidget(newRowIndex, 5, manufacturerCell)
		self.setCellWidget(newRowIndex, 6, originCell)

	@pyqtSlot(object)
	def pidInput(self, cell):
		if cell.isEmpty():
			cell.valid = False
			return

		# Todo: Do a network call for a collision check		

	@pyqtSlot(object)
	def nameInput(self, cell):
		cell.valid = not cell.isEmpty()

	@pyqtSlot(object)
	def formatInput(self, cell):
		cell.valid = not cell.isEmpty()

	@pyqtSlot(object)
	def unitInput(self, cell):
		cell.valid = not cell.isEmpty()

	@pyqtSlot(object)
	def manufacturerInput(self, cell):
		cell.valid = not cell.isEmpty()

	@pyqtSlot(object)
	def originInput(self, cell):
		cell.valid = not cell.isEmpty()