from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout

from view.prompt.abstractedprompt import AbstractedPrompt

import gettext
_ = gettext.gettext

class NewClientPrompt(AbstractedPrompt):
	def __init__(self, controller, client):
		super().__init__(client)
		self.controller = controller
		self.setWindowTitle(_('New Client'))

		# Set layout
		self.resize(1000,600)
		self.layout = QHBoxLayout()
		self.setLayout(self.layout)

		# self.table = None
		self.control = QVBoxLayout()

		# self.layout.addWidget(self.table)
		self.layout.addStretch(4)
		self.layout.addLayout(self.control,1)

		# Control panel
		self.delete = QPushButton(_('Delete'))
		self.confirm = QPushButton(_('Confirm'))
		self.cancel = QPushButton(_('Cancel'))

		self.control.addStretch(5)
		self.control.addWidget(self.delete)
		self.control.addStretch(6)
		self.control.addWidget(self.confirm)
		self.control.addWidget(self.cancel)

		