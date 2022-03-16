import logging
import traceback
import sys

from PyQt5.QtWidgets import QApplication
from app import Application

class Main:
	def __init__(self):
		self.environment = QApplication([])
		self.environment.setStyle('Fusion')
		self.app = Application(self)

	def exec(self):
		try:
			self.app.exec()
		except Exception as e:
			msg = traceback.format_exc()
			logging.critical('Application crashed\n{}'.format(msg))

	def reboot(self):
		del self.app
		self.app = Application(self)
		self.exec()

	def restartClient(self):
		self.app.startClient()

	def exit(self):
		sys.exit()

main = Main()
main.exec()