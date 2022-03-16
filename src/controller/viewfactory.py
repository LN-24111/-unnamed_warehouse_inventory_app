from view.mainclient import Client
from view.tabs.importtab import ImportTab
from view.tabs.components import *

from view.prompt.simpleprompts import *
from view.prompt.newproduct import NewProductPrompt
from view.prompt.newclient import NewClientPrompt

from view.table.newproduct import NewProductTable

import gettext
_ = gettext.gettext

class ViewFactory:
	def __init__(self, settings, database, main):
		self.settings = settings
		self.database = database
		self.main = main


#================================================== Prompts ==================================================#
	def buildConfirmPrompt(self, message=_('Confirm?')):
		return ConfirmPrompt(message, self.main.getClient())

	def buildMessagePrompt(self, message):
		return MessagePrompt(message, self.main.getClient())

	def buildNewProductPrompt(self):
		# TODO
		return NewProductPrompt(None, self.main.getClient())

	def buildNewClientPrompt(self):
		# TODO
		return NewClientPrompt(None, self.main.getClient())

#================================================== Main window ==================================================#
	def buildMainClient(self):
		return Client(self.settings, self)	

	#==================== Import tab ====================#
	def buildImportTab(self):
		return ImportTab(self.settings, self)

	def buildClientBox(self):
		# Todo: hook up a controller here
		return ClientBox(None, self)

	def buildProductBox(self):
		return ProductBox(self)

	def buildBillingBox(self):
		# Hook up a controller here
		return BillingBox(None)



	def buildExportTab(self):
		pass

	def buildModifyTab(self):
		pass

	def buildViewTab(self):
		pass

	def buildSalesTab(self):
		pass

	def buildSettingsTab(self):
		pass

	#==================== Tables ====================#
	def buildNewProductTable(self):
		# TODO: Add controller
		table = NewProductTable(None, None)
		return table	



	