from PyQt5.QtWidgets import QComboBox

class ComboBoxCell(QComboBox):
	@property
	def valid(self):
		return self.currentText() != ''