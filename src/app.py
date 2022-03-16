from model.settings import Settings
from model.dao import DAOFactory
from database.mongo import MongoDatabase
from controller.viewfactory import ViewFactory

from view.prompt.login import LoginPrompt
from view.prompt.simpleprompts import MessagePrompt


class Application:
	def __init__(self, main):
		self.main = main

		# Declare all the attributes. We will assign them later
		self.settings = None
		self.mongo = None
		self.database = None
		self.viewFactory = None

		# Views
		self.loginPrompt = None
		self.client = None

	def login(self, username, password):
		# Initialize core components
		self.settings = Settings(username, password, self.main)
		try:
			self.mongo = MongoDatabase(self.settings) 
			self.mongo.authenticate()
		except:
			self.main.reboot()

		# Initialize assembled components
		self.database = DAOFactory(self.settings, self.mongo)
		self.viewFactory = ViewFactory(self.settings, self.database, self.main)

		# Start the client
		self.startClient()

	def exec(self):
		self.loginPrompt = LoginPrompt()
		self.loginPrompt.cancelSignal.connect(lambda x: self.main.exit())
		self.loginPrompt.submitSignal.connect(self.login)
		self.loginPrompt.show()

	def startClient(self):
		del self.client
		self.client = self.viewFactory.buildMainClient()
		self.client.show()

	def getClient(self):
		return self.client