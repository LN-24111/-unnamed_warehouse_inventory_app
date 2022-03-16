from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QTabWidget, QWidget, QDesktopWidget, QVBoxLayout

import gettext
_ = gettext.gettext

class Client(QWidget):
	def __init__(self, settings, viewFactory):
		super().__init__()
		self.settings = settings
		self.viewFactory = viewFactory

		self.setGeometry (QDesktopWidget().availableGeometry())
		self.setWindowTitle(_('Inventory Management'))
		self.setFocusPolicy(Qt.ClickFocus)

		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.tabs = QTabWidget()	
		self.layout.addWidget(self.tabs)

		# Add tabs
		self.importTab = self.viewFactory.buildImportTab()
		self.exportTab = QWidget()
		self.modifyTab = QWidget()
		self.logsTab = QWidget()
		self.settingTab = QWidget()

		self.tabs.addTab(self.importTab, _('Import'))
		self.tabs.addTab(self.exportTab, _('Export'))
		self.tabs.addTab(self.modifyTab, _('Modify'))
		self.tabs.addTab(self.logsTab, _('Logs'))
		self.tabs.addTab(self.settingTab, _('Settings'))

		# self.tabs.currentChanged.connect(lambda x : self.tabs.widget(x).refresh())

	def keyPressEvent(self, e):
		if e.key() == Qt.Key_F11:
			if self.isFullScreen():
				self.showNormal()
			else:
				self.showFullScreen()

	def freeze(self):
		self.setEnabled(False)

	def resume(self):
		self.setEnabled(True)