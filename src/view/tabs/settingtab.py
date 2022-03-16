from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QCheckBox, QPushButton, QGroupBox
import gettext
from view.simpleprompt import ConfirmPrompt, MessagePrompt


_ = gettext.gettext

class SettingTab(QWidget):
	restartRequest = pyqtSignal()

	def __init__(self, settings):
		super().__init__(parent)

		self.settings = settings

		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.general = QGroupBox(_('General'))
		self.layout.addWidget(self.general)
		self.addGeneralSettings()

		self.impExp = QGroupBox(_('Import/Export'))
		self.layout.addWidget(self.impExp)
		self.addImportExportSettings()

		self.apply = QPushButton(_('Apply'))
		self.layout.addWidget(self.apply)
		self.apply.clicked.connect(self.applySettings)

		self.layout.addStretch(1)
		self.refresh()

	def refresh(self):
		conf = self.settings.values

		if conf['general_language'] == 'en':
			self.general.en.setChecked(True)
		if conf['general_language'] == 'vn':
			self.general.vn.setChecked(True)

		self.impExp.calendar.setChecked(conf['import_UseCalendar'])
		self.impExp.importIDNew.setChecked(conf['import_IDNew'])
		self.impExp.importIDFind.setChecked(conf['import_IDFind'])
		self.impExp.exportIDFind.setChecked(conf['export_IDFind'])


	@pyqtSlot()
	def applySettings(self):
		conf = {}

		if self.general.en.isChecked():
			conf['general_language'] = 'en'
		if self.general.vn.isChecked():
			conf['general_language'] = 'vn'

		conf['import_UseCalendar'] = self.impExp.calendar.isChecked()
		conf['import_IDNew'] = self.impExp.importIDNew.isChecked()
		conf['import_IDFind'] = self.impExp.importIDFind.isChecked()
		conf['export_IDFind'] = self.impExp.exportIDFind.isChecked()

		if conf['general_language'] != self.settings.values['general_language']:
			self.prompt = ConfirmPrompt(_('Language change will be applied on restart. Restart app now?'))
			self.prompt.confirm.connect(lambda : self.restartRequest.emit())
		else:
			self.prompt = MessagePrompt(_('Settings saved'))
	
		self.settings.values = conf
		self.refresh
		self.prompt.show()

	def addGeneralSettings(self):
		e = self.general
		e.layout = QVBoxLayout()
		e.setLayout(e.layout)

		e.langLabel = QLabel(_('Languages'))
		e.layout.addWidget(e.langLabel)

		e.languages = QHBoxLayout()
		e.layout.addLayout(e.languages)

		e.en = QRadioButton('English')
		e.languages.addWidget(e.en)

		e.vn = QRadioButton('Tiếng Việt')
		e.languages.addWidget(e.vn)


	def addImportExportSettings(self):
		e = self.impExp
		e.layout = QVBoxLayout()
		e.setLayout(e.layout)

		e.calendar = QCheckBox(_('Enable calendar widget to select date'))
		e.layout.addWidget(e.calendar)

		e.importID = QHBoxLayout()
		e.layout.addLayout(e.importID)

		e.importIDNew = QCheckBox(_('Import: Create new entry for unrecognized ID'))
		e.importID.addWidget(e.importIDNew)

		e.importIDFind = QCheckBox(_('Import: Find entry for unrecognized ID'))
		e.importID.addWidget(e.importIDFind)

		e.importIDNew.stateChanged.connect(lambda x : e.importIDFind.setCheckState(0 if x == 2 else e.importIDFind.checkState()))
		e.importIDFind.stateChanged.connect(lambda x : e.importIDNew.setCheckState(0 if x == 2 else e.importIDNew.checkState()))

		e.exportIDFind = QCheckBox(_('Export: Find entry for unrecognized ID'))
		e.layout.addWidget(e.exportIDFind)