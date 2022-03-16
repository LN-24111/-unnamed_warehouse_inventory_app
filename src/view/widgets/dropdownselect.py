from PyQt5.QtCore import Qt, pyqtSlot, QItemSelectionModel
from PyQt5.QtWidgets import QLineEdit, QCompleter

class DropDownSelect(QLineEdit):
	def __init__(self, lst):
		super().__init__()
		self.updateCompleter(lst)
		self.lastText = ''

		self.editingFinished.connect(self.deFocus)

	def deFocus(self, *args):
		if self.text() not in self.lst:
			self.setText(self.lastText)
		else:
			self.lastText = self.text()

		self.clearFocus()

	def updateCompleter(self, lst):
		self.lst = lst

		self.completer = QCompleter(lst)
		self.completer.setCaseSensitivity(Qt.CaseInsensitive)
		self.setCompleter(self.completer)

		if self.text() not in lst:
			self.setText('')
			self.lastText = ''