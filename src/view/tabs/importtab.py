from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QCompleter, QLineEdit, QLabel, QWidget, QHBoxLayout, QTableWidget, QHeaderView, QVBoxLayout, QPushButton, QSpinBox, QTableWidgetItem, QGroupBox, QComboBox

import gettext
_ = gettext.gettext

class ImportTab(QWidget):

	def __init__(self, settings, viewFactory):
		super().__init__()
		self.settings = settings
		self.viewFactory = viewFactory

		self.layout = QHBoxLayout()
		self.setLayout(self.layout)

		# Divide area for table and for control panel
		self.table = QWidget()
		self.panel = QVBoxLayout()

		self.layout.addWidget(self.table, 4)
		self.layout.addLayout(self.panel, 1)

		# Draw control panel
		self.clientBox = self.viewFactory.buildClientBox()
		self.productBox = self.viewFactory.buildProductBox()
		self.billingBox = self.viewFactory.buildBillingBox()

		self.buttons = QHBoxLayout()

		self.clear = QPushButton(_('Clear'))
		self.submit = QPushButton(_('Submit'))

		self.buttons.addWidget(self.clear)
		self.buttons.addWidget(self.submit)

		self.panel.addStretch(2)
		self.panel.addWidget(self.clientBox)
		self.panel.addWidget(self.productBox)
		self.panel.addStretch(6)
		self.panel.addWidget(self.billingBox)
		self.panel.addLayout(self.buttons)
		
		# Define button functions
		self.submit.clicked.connect(self.submitForm)
		self.clear.clicked.connect(self.clearConfirm)

	def clearConfirm(self):
		self.clearPrompt = self.viewFactory.buildConfirmPrompt(_('This will erase all your current work.'))
		self.clearPrompt.confirm.connect(self.clearForm)
		self.clearPrompt.show()

	def clearForm(self):
		pass

	def submitForm(self):
		pass

