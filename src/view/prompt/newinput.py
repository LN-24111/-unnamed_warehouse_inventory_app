class NewInputPrompt(CenterWidget):
	closeSignal = pyqtSignal()
	dataSignal = pyqtSignal(dict)
	def __init__(self, inflater, controller):
		super().__init__()
		self.inflater = inflater
		self.controller = controller

		# General setups
		self.layout = QVBoxLayout()
		self.resize(800,400)
		self.setLayout(self.layout)
		
		self.table = Table(inflater)
		self.layout.addWidget(self.table)
		self.table.addLine(1)

		self.control = QHBoxLayout()
		self.layout.addLayout(self.control)

		self.addLine = QPushButton(_('Add'))
		self.control.addWidget(self.addLine)
		self.addLine.clicked.connect(lambda : self.table.addLine(self.spinbox.value()))

		self.spinbox = QSpinBox()
		self.control.addWidget(self.spinbox)
		self.spinbox.setValue(1)

		self.delete = QPushButton(_('Delete'))
		self.control.addWidget(self.delete)
		self.delete.clicked.connect(self.table.deleteSlot)

		self.confirmCancel = QHBoxLayout()
		self.layout.addLayout(self.confirmCancel)

		self.confirm = QPushButton(_('Confirm'))
		self.confirmCancel.addWidget(self.confirm)
		self.confirm.clicked.connect(self.confirmSlot)

		self.cancel = QPushButton(_('Cancel'))
		self.confirmCancel.addWidget(self.cancel)
		self.cancel.clicked.connect(self.cancelSlot)


	@pyqtSlot()
	def confirmSlot(self):
		f = True

		self.table.disableInputCheck()
		for i in range(self.table.rowCount()):
			for j in self.inflater.getImportantKeys():
				item = self.table.item(i, self.inflater.getTitles().index(j))

				if item.text() == '':
					item.setBackground(Qt.red)
					f = False
		self.table.enableInputCheck()
		
		# Parsing table data
		if f:
			for i in range(self.table.rowCount()):
				row = {}
				for j in range(self.table.columnCount()):
					item = self.table.item(i, j)
					text = item.text()
					row[self.inflater.getTitles()[j]] = text
				# Interact with data model
				self.controller.process(row)
				# Broadcast data to anything else that might need it
				self.dataSignal.emit(row)
			self.close()

	@pyqtSlot()
	def cancelSlot(self):
		self.close()

	def closeEvent(self, event):
		self.closeSignal.emit()