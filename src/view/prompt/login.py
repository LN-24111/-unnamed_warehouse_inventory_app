from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSignal, QMargins
from view.prompt.simpleprompts import CenterWidget
import gettext
_ = gettext.gettext

class LoginPrompt(CenterWidget):
	submitSignal = pyqtSignal(str, str)
	cancelSignal = pyqtSignal()
	
	def __init__(self):
		super().__init__()
		self.setWindowTitle(_('Login'))

		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.layout.setContentsMargins(20,15,20,10)
		self.setFixedWidth(300)

		self.userError = QLabel()
		self.layout.addWidget(self.userError)
		self.userError.setWordWrap(True)
		self.userError.hide()

		self.username = QLineEdit()
		self.username.setPlaceholderText(_('username'))
		self.username.setTextMargins(QMargins(5,0,0,0))
		self.layout.addWidget(self.username)

		self.pwdError = QLabel()
		self.layout.addWidget(self.pwdError)
		self.pwdError.hide()

		self.password = QLineEdit()
		self.password.setPlaceholderText(_('password'))
		self.password.setTextMargins(QMargins(5,0,0,0))
		self.password.setEchoMode(QLineEdit.Password)
		self.layout.addWidget(self.password)

		self.username.returnPressed.connect(self.formSubmission)
		self.password.returnPressed.connect(self.formSubmission)

		self.submitted = False


	def formSubmission(self):
		usr = self.username.text()
		pwd = self.password.text()
		self.password.setStyleSheet('')
		self.pwdError.hide()
		self.username.setStyleSheet('')
		self.userError.hide()
		
		usr_flag = False
		pwd_flag = False

		import re
		
		if re.match('^[a-zA-Z][a-zA-Z0-9]+$', usr):
			if len(usr) > 20:
				self.userError.setText(_('Username must be at most 20 characters'))

				usr_flag = True
		else:
			self.userError.setText(_('Username must contain only letters and numbers, and cannot start with a number'))
			usr_flag = True

		if len(pwd) < 6:
			self.pwdError.setText(_('Password must be at least 6 characters'))
			pwd_flag = True

		if pwd_flag:
			self.password.setStyleSheet('QLineEdit{background: red}')
			self.pwdError.show()

		if usr_flag:
			self.username.setStyleSheet('QLineEdit{background: red}')
			self.userError.show()

		if not usr_flag and not pwd_flag:
			self.submitSignal.emit(self.username.text(), self.password.text())
			self.submitted = True
			self.close()

	def closeEvent(self, event):
		if not self.submitted:
			self.cancelSignal.emit()