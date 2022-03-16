from controller.abstractedcontroller import AbstractedViewController
from controller.error import Error

class EditTransactionController(AbstractedViewController):
	def __init__(self, database, transactionFactory, logger):
		self.database = database.createTransactionAccessObject()
		self.transactionFactory = transactionFactory
		self.logger = logger

	def process(self, rawDatas, sid):
		
		updateTransactions = []
		for data in rawDatas:
			transaction = self.transactionFactory.build({
				'CID': data['new']['CID'],
				'Amount': data['new']['Amount'],
				'Type': 'Payment'	#Cannot edit import/export transaction, they're automated
			})
			updateTransactions.append({
				'old': data['old'],
				'new': transaction
			})

		try:
			self.dao.setItems(updateTransactions)

			self.logger.logUpdate(updateTransactions)
		except:
			return Error.NETWORK

		return Error.NONE

	def delete(self, datas):
		self.dao = self.database.createTransactionAccessObject()

		try:
			self.dao.delete(datas)

			self.logger.logDelete(datas)
		except:
			return Error.NETWORK

		return Error.NONE

	def getDatas(self, _filter):
		self.dao = self.database.createTransactionAccessObject()
		
		try:
			datas = self.dao.getItems(_filter)
			return datas
		except:
			return Error.NETWORK