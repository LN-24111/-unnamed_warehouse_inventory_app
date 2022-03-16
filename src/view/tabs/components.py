from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QLineEdit, QCompleter, QComboBox, QVBoxLayout, QGroupBox, QHBoxLayout, QPushButton, QLabel

from view.widgets.dropdownselect import DropDownSelect

import gettext
_ = gettext.gettext

class ClientBox(QGroupBox):
	def __init__(self, controller, viewFactory):
		super().__init__(_('Client'))
		self.controller = controller
		self.viewFactory = viewFactory

		# Set layout
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		# Draw the box components
		self.select = DropDownSelect([])
		self.addClients = QPushButton(_('Add new clients'))

		self.layout.addWidget(self.select)
		self.layout.addWidget(self.addClients)

		# Link button
		self.addClients.clicked.connect(self.createNewClientPrompt)

		self.updateComboBox()

	def updateComboBox(self, *args):
		pass

	def createNewClientPrompt(self):
		self.clientPrompt = self.viewFactory.buildNewClientPrompt()
		self.clientPrompt.show()

	def getCID(self):
		return self.text()

class ProductBox(QGroupBox):
	def __init__(self, viewFactory):
		super().__init__(_('Product'))
		self.viewFactory = viewFactory

		# Set layout
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		# Draw the box components
		self.addProducts = QPushButton(_('Add new products'))
		self.layout.addWidget(self.addProducts)

		# Connect the button
		self.addProducts.clicked.connect(self.createNewProductPrompt)

	def createNewProductPrompt(self):
		self.productPrompt = self.viewFactory.buildNewProductPrompt()
		self.productPrompt.show()

class BillingBox(QGroupBox):
	def __init__(self, controller):
		super().__init__(_('Billing'))
		self.controller = controller

		# Set layout
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		# Draw components
		self.paymentLine = QHBoxLayout()
		
		self.paymentLabel = QLabel(_('Payment:'))
		self.paymentLabel.setStyleSheet('font-weight: bold')
		self.paymentBox = QLineEdit()
		self.paymentBox.setAlignment(Qt.AlignRight)
		self.paymentBox.setValidator(QIntValidator())
		self.paymentBox.editingFinished.connect(self.paymentBox.clearFocus)
		# I blame Qt
		self.paymentBox.textEdited.connect(lambda *args: self.paymentBox.setText('{:,}'.format(int(('0' + self.paymentBox.text()).replace(',','')))))

		self.paymentLine.addWidget(self.paymentLabel)
		self.paymentLine.addWidget(self.paymentBox)


		self.totalLine = QHBoxLayout()

		self.totalLabel = QLabel(_('Total:'))
		self.totalLabel.setStyleSheet('font-weight: bold')
		self.total = QLabel()
		self.total.setStyleSheet('font-weight: bold')
		self.total.setAlignment(Qt.AlignRight)

		self.totalLine.addWidget(self.totalLabel)
		self.totalLine.addWidget(self.total)


		self.layout.addLayout(self.paymentLine)
		self.layout.addLayout(self.totalLine)

	def setTotal(self, total):
		self.total.setText(str(total))

	def submit(self, cid):
		pass