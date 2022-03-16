from PyQt5.QtCore import Qt, pyqtSlot, QMargins, pyqtSignal, QDate
from PyQt5.QtWidgets import QScrollArea, QPushButton, QWidget, QDesktopWidget, QVBoxLayout, QHBoxLayout, QCalendarWidget, QLabel

from view.prompt.abstractedprompt import AbstractedPrompt

import sys
import gettext
_ = gettext.gettext

# LEGACY CODE
class MessagePrompt(AbstractedPrompt):
	def __init__(self, message, client):
		super().__init__(client)

		self.setFixedWidth(200)
		self.setMinimumHeight(120)
		self.setWindowTitle(_('Alert'))
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.label = QLabel(message)
		self.layout.addWidget(self.label)
		self.layout.setAlignment(self.label, Qt.AlignHCenter)
		self.label.setWordWrap(True)

		self.button = QPushButton(_('Ok'))
		self.layout.addWidget(self.button)
		self.layout.setAlignment(self.button, Qt.AlignHCenter)
		self.button.setFixedWidth(100)
		self.button.clicked.connect(self.close)

class ConfirmPrompt(AbstractedPrompt):
	confirm = pyqtSignal()
	cancel = pyqtSignal()

	def __init__(self, message, client):
		super().__init__(client)

		self.setFixedWidth(240)
		self.setMinimumHeight(120)
		self.setWindowTitle(_('Confirm'))
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.label = QLabel(message)
		self.layout.addWidget(self.label)
		self.label.setWordWrap(True)
		self.layout.setAlignment(self.label, Qt.AlignHCenter)

		self.bLayout = QHBoxLayout()
		self.layout.addLayout(self.bLayout)


		self.confirmButton = QPushButton(_('Ok'))
		self.confirmButton.clicked.connect(self.confirmButtonSlot)
		self.bLayout.setContentsMargins(15, 10, 15, 0)
		self.confirmed = False

		self.cancelButton = QPushButton(_('Cancel'))
		self.cancelButton.clicked.connect(lambda : self.close())
		self.bLayout.setContentsMargins(15, 10, 15, 0)

		self.bLayout.addWidget(self.cancelButton)
		self.bLayout.addWidget(self.confirmButton)

	@pyqtSlot()
	def confirmButtonSlot(self):
		self.confirm.emit()
		self.confirmed = True
		self.close()

	def closeEvent(self, event):
		if not self.confirmed:
			self.cancel.emit()
		super().closeEvent(event)

class TimeSelect(AbstractedPrompt):
	callback = pyqtSignal(object, str)

	def __init__(self, item, client):
		super().__init__(client)

		self.item = item
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.calendar = QCalendarWidget()
		self.layout.addWidget(self.calendar)
		self.calendar.activated.connect(self.dateSelect)

	@pyqtSlot(QDate)
	def dateSelect(self, date):
		self.callback.emit(self.item, date.toString('yyyy-MM-dd'))
		self.close()

class SelectPrompt(AbstractedPrompt):
	def __init__(self, client):
		super().__init__(client)
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.table = QTableWidget()
		self
		self.scroll = QScrollArea()
		self.layout.addWidget(self.scroll)
		self.scroll.setWidgetResizable(True)

		self.scroll.wrapper = QWidget()

		self.scroll.wrapperLayout = QVBoxLayout()
		self.scroll.wrapper.setLayout(self.scroll.wrapperLayout)

		self.scroll.wrapperLayout.addStretch(0)
		self.scroll.setWidget(self.scroll.wrapper)

	def add(self):
		btn = QPushButton('x')
		self.scroll.wrapperLayout.insertWidget(0, btn)
		btn.setFlat(True)
		btn.clicked.connect(btn.hide)

		return btn