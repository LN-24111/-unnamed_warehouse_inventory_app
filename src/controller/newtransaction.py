from controller.abstractedcontroller import AbstractedViewController
from controller.error import Error

class NewTransactionController(AbstractedViewController):
	def __init__(self, database, transactionFactory, logger):
		self.dao = database.createTransactionAccessObject()
		self.transactionFactory = transactionFactory
		self.logger = logger

	def process(self, rawDatas):
		timestamp = self._createTimeStamp()

		newTransactions = []
		for data in rawDatas:
			transaction = self.transactionFactory.build({
				'CID': data['CID'],
				'Amount': data['Amount'],
				'Type': 'Payment'
			}, timestamp)

		try:
			self.dao.addItems(newTransactions)

			self.logger.logUpdate(newTransactions)
		except:
			return Error.NETWORK

		return Error.NONE