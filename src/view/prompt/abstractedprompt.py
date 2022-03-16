from PyQt5.QtWidgets import QWidget, QDesktopWidget

class AbstractedPrompt(QWidget):
	def __init__(self, client):
		super().__init__()
		self.client = client
		self.client.freeze()

	def show(self):
		super().show()
		self.center()

	def center(self):
		qr = self.geometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def closeEvent(self, event):
		self.client.resume()
		super().closeEvent(event)