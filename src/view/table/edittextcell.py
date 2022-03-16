from PyQt5.Qt import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QLineEdit

class EditTextCell(QLineEdit):
	newUserInput = pyqtSignal(object)

	# The valid flag is set by the table to indicate validity of a cell
	# A row can be parsed only if every cell is valid
	@property
	def valid(self):
		return self._valid

	@valid.setter
	def valid(self, valid):
		self._valid = valid	

	# Empty does not indicate invalid, so it's separated
	# A row is empty if every cell is empty
	# A row that's neither empty nor valid is flagged to user
	def isEmpty(self):
		return self.text() == ''

	# Valid is True for non important fields
	def __init__(self, valid=False):
		super().__init__()
		self.lastInput = ''
		self._valid = valid
		self.editingFinished.connect(self.verifyNewInput)

	@pyqtSlot()
	def verifyNewInput(self):
		if self.lastInput != self.text():
			self.lastInput = self.text()
			self.newUserInput.emit(self)