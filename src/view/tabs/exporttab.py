from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget, QHBoxLayout, QTableWidget, QHeaderView, QVBoxLayout, QPushButton, QSpinBox, QTableWidgetItem, QGroupBox, QComboBox
from view.prompt import TimeSelect, NewCustomerPrompt
import time
import sys
import gettext

_ = gettext.gettext

class ExportTab(QWidget):

	def __init__(self, settings, database, parent = None):
		super().__init__(parent)

		self.settings = settings
		self.database = database

		self.layout = QHBoxLayout()
		self.setLayout(self.layout)

		self.table = QTableWidget(0, 11)
		self.layout.addWidget(self.table, 4)
		self.table.setHorizontalHeaderLabels([_('ID'),_('Product'),_('Format'),_('Unit'),_('Qty'),_('Price'),_('VAT'),_('Total'),_('Expire'),_('Manufacturer'),_('Origin')])
		self.columnLabels = ['ID', 'Name', 'Format', 'Unit', 'Quantity', 'Price', 'VAT', 'Total', 'Expire', 'Manufacturer', 'Origin']
		self.keyColumns = ['ID', 'Quantity', 'Price']
		self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
		self.table.horizontalHeader().setStretchLastSection(True)
		self.table.itemChanged.connect(self.userInputSlot)
		self.table.setColumnWidth(self.columnLabels.index('ID'), 80)
		self.table.setColumnWidth(self.columnLabels.index('Name'), 100)
		self.table.setColumnWidth(self.columnLabels.index('Format'), 140)
		self.table.setColumnWidth(self.columnLabels.index('Unit'), 60)
		self.table.setColumnWidth(self.columnLabels.index('Quantity'), 60)
		self.table.setColumnWidth(self.columnLabels.index('Price'), 90)
		self.table.setColumnWidth(self.columnLabels.index('VAT'), 90)
		self.table.setColumnWidth(self.columnLabels.index('Total'), 110)
		self.table.setColumnWidth(self.columnLabels.index('Expire'), 90)
		self.table.setColumnWidth(self.columnLabels.index('Manufacturer'), 100)
		self.clickedItem = None

		self.control = QVBoxLayout()
		self.layout.addLayout(self.control, 1)
		self.initControlPanel()

	def refresh(self):
		pass

	def initControlPanel(self):
		self.control.addStretch(3)

		self.customer = QGroupBox(_('Customer'))
		self.control.addWidget(self.customer)

		self.customer.layout = QVBoxLayout()
		self.customer.setLayout(self.customer.layout)

		self.customerSelect = QComboBox()
		self.customer.layout.addWidget(self.customerSelect)
		self.customerSelect.setEditable(True)

		self.customerNew = QPushButton(_('Add new customer'))
		self.customer.layout.addWidget(self.customerNew)
		self.customerNew.clicked.connect(self.newCustomerSlot)
		self.newCustomerPrompt = None

		self.control.addStretch(1)

		self.inventory = QGroupBox(_('Inventory'))
		self.control.addWidget(self.inventory)

		self.inventory.layout = QVBoxLayout()
		self.inventory.setLayout(self.inventory.layout)

		self.selectInventories = QPushButton(_('Select Inventories'))
		self.inventory.layout.addWidget(self.selectInventories)
		self.selectInventories.clicked.connect(self.selectInventoriesSlot)

		self.addLine = QHBoxLayout()
		self.inventory.layout.addLayout(self.addLine)

		self.addBtn = QPushButton(_('Add line'))
		self.addLine.addWidget(self.addBtn)
		self.addBtn.clicked.connect(self.addSlot)

		self.spinbox = QSpinBox()
		self.addLine.addWidget(self.spinbox)
		self.spinbox.setValue(1)

		self.delete = QPushButton(_('Delete Line'))
		self.inventory.layout.addWidget(self.delete)
		self.delete.clicked.connect(self.deleteSlot)

		self.control.addStretch(2)

		self.billing = QGroupBox(_('Billing'))
		self.control.addWidget(self.billing)

		self.billing.layout = QVBoxLayout()
		self.billing.setLayout(self.billing.layout)

		self.billDate = QHBoxLayout()
		self.billing.layout.addLayout(self.billDate)

		self.billDateLabel = QLabel(_('Date:'))
		self.billDate.addWidget(self.billDateLabel)

		self.billDate.addStretch(1)

		self.billDateSelect = QPushButton(time.strftime('%Y-%m-%d', time.localtime()))
		self.billDate.addWidget(self.billDateSelect)
		self.billDateSelect.setFlat(True)
		self.billDateSelect.clicked.connect(lambda : self.timePrompt(self.billDateSelect))

		self.billIDLine = QHBoxLayout()
		self.billing.layout.addLayout(self.billIDLine)

		self.billIDLabel = QLabel(_('Bill ID:'))
		self.billIDLine.addWidget(self.billIDLabel)

		self.billIDBox = QLineEdit()
		self.billIDLine.addWidget(self.billIDBox)
		self.billIDBox.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

		self.billPayLine = QHBoxLayout()
		self.billing.layout.addLayout(self.billPayLine)

		self.billPayLabel = QLabel(_('Paid amount:'))
		self.billPayLine.addWidget(self.billPayLabel)

		self.billPayBox = QLineEdit()
		self.billPayLine.addWidget(self.billPayBox)
		self.billPayBox.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

		self.billTotalLine = QHBoxLayout()
		self.billing.layout.addLayout(self.billTotalLine)

		self.billTotalLabel = QLabel(_('Total:'))
		self.billTotalLine.addWidget(self.billTotalLabel)
		self.billTotalLabel.setStyleSheet("font-weight: bold")

		self.billTotalLine.addStretch(1)

		self.billTotalAmount = QLabel('0')
		self.billTotalLine.addWidget(self.billTotalAmount)
		self.billTotalAmount.setStyleSheet("font-weight: bold")

		self.submit = QPushButton(_('Submit'))
		self.control.addWidget(self.submit)
		self.submit.clicked.connect(self.submitSlot)

# ================================================= Table scripts ================================================= #

	@pyqtSlot()
	def addSlot(self):
		amount = self.spinbox.value()
		current = self.table.rowCount()
		self.table.setRowCount(current + amount)

		for i in range(current, current + amount):
			for j in range(self.table.columnCount()):
				item = QTableWidgetItem()
				if not self.columnLabels[j] in self.keyColumns:
					item.setFlags(item.flags() ^ Qt.ItemIsEditable)
					item.setBackground(Qt.gray)
					item.setTextAlignment(Qt.AlignVCenter)
				else:
					item.setTextAlignment(Qt.AlignCenter)

				if self.columnLabels[j] in ['Price', 'Total']:
					item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

				self.table.setItem(i, j, item)
		self.table.setCurrentItem(self.table.item(current, 0))

	@pyqtSlot(QTableWidgetItem)
	def userInputSlot(self, item):
		if item.text() == '':
			return

		label = self.columnLabels[item.column()]
		if label in ['Price', 'Quantity']:
			try:
				if label == 'Price':
					val = float(item.text().replace(',',''))
					otherCol = self.columnLabels.index('Quantity')
				else:
					val = int(item.text().replace(',',''))
					otherCol = self.columnLabels.index('Price')
				item.setBackground(Qt.white)
				item.setText("{:,}".format(val))
				try:
					val2 = float(self.table.item(item.row(), otherCol).text().replace(',',''))
					print (val2)
					self.table.item(item.row(), self.columnLabels.index('Total')).setText("{:,}".format(val * val2))
				except:
					pass
			except:
				if item.text() != '':
					item.setBackground(Qt.red)
			finally:
				total = 0
				for i in range(self.table.columnCount()):
					try:
						total += float(self.table.item(i, self.columnLabels.index('Total')).text().replace(',',''))
					except:
						pass
				self.billTotalAmount.setText("{:,}".format(total))

		if label == 'ID':
			if True:
				if self.settings.values['export_IDFind']:
					pass
				else:
					item.setText('')
			else:
				pass

		if label == 'Expire':
			from time import strptime, strftime
			possibleFormats = {'%Y:%m:%d', '%d:%m:%Y', '%Y/%m/%d', '%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y'}
			f = True
			for f in possibleFormats:
				try:
					date = strftime('%Y-%m-%d', strptime(item.text(), f))
					f = False
					item.setText(date)
					break
				except:
					pass
			if f:
				item.setBackground(Qt.red)
			else:
				item.setBackground(Qt.white)

	def timePrompt(self, item):
		self.clickedItem = item
		self.setEnabled(False)
		self.timeSelect = TimeSelect()
		self.timeSelect.closeSignal.connect(self.resumeExec)
		self.timeSelect.callback.connect(self.dateSelected)
		self.timeSelect.show()

	@pyqtSlot(str)
	def dateSelected(self, date):
		self.clickedItem.setText(date)

	@pyqtSlot(list)
	def IDSlot(self, data):
		self.clickedItem.setText(data[0]['ID'])

# ================================================= Button scripts ================================================= #
	@pyqtSlot()
	def resumeExec(self):
		if isinstance(self.clickedItem , QTableWidgetItem):
			self.table.setCurrentItem(self.table.itemAt(0,0))
			self.table.setCurrentItem(self.clickedItem)
		self.setEnabled(True)

	# ======================== New Customer Button ======================== #
	@pyqtSlot()
	def newCustomerSlot(self):
		if self.newCustomerPrompt is None:
			self.newCustomerPrompt = NewCustomerPrompt()
			self.newCustomerPrompt.closeSignal.connect(self.ncpCloseSlot)
			self.newCustomerPrompt.formSubmissionSignal.connect(self.ncpDataSlot)
		self.newCustomerPrompt.show()
		self.newCustomerPrompt.setWindowState(self.newCustomerPrompt.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
		self.newCustomerPrompt.activateWindow()

	@pyqtSlot()
	def ncpCloseSlot(self):
		self.newCustomerPrompt = None

	@pyqtSlot(list)
	def ncpDataSlot(self, data):
		print (data)

	# ======================== Select Inventories Button ======================== #
	@pyqtSlot()
	def selectInventoriesSlot(self):
		pass

	# ======================== Delete Button ======================== #

	@pyqtSlot()
	def deleteSlot(self):
		lst = set()
		for i in self.table.selectedIndexes():
			lst.add(i.row())

		j = 0
		for i in lst:
			self.table.removeRow(i - j)
			j += 1

	# ======================== Submit Button ======================== #
	@pyqtSlot()
	def submitSlot(self):
		pass