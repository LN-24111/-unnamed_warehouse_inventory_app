from controller.abstractedcontroller import AbstractedViewController
from controller.error import Error

class EditImportController(AbstractedViewController):
	def __init__(self, database, importFactory, transactionFactory, logger):
		self.database = database
		self.importFactory = importFactory
		self.transactionFactory = transactionFactory
		self.logger = logger

	def process(self, rawDatas, sid):
		importDAO = self.database.createImportAccessObject()
		transactionDAO = self.database.createTransactionAccessObject()


		# Update the import database
		update = []
		for data in rawDatas:
			# Extract the timestamp
			timestamp = data['old'].data['Date']
			
			newData = self.importFactory.build(data['new'], timestamp)

			if newData != data['old']:
				update.append({
					'old': data['old'],
					'new': newData
					})

			total+= data['new']['Qty'] * data['new']['Price']

		# Update the transaction database
		newTransaction = self.transactionFactory.build({
			'CID': sid,
			'Date': timestamp,
			'Amount': total,
			'Type': 'Import'
		})

		oldTransaction = transactionDAO.getItems({
			'Date': timestamp,
			'Type': 'Import'
		})[0]

		updateTransaction = {
			'old': oldTransaction,
			'new': newTransaction
		}

		try:
			importDAO.setItems(update)
			transactionDAO.setItems(updateTransaction)

			self.logger.logUpdate(update)
		except:
			return Error.NETWORK

		return Error.NONE

	def delete(self, datas):
		importDAO = self.database.createImportAccessObject()

		try:
			importDAO.delete(datas)
			self.logger.logDelete(datas)
		except:
			return Error.NETWORK

		return Error.NONE

	def getDatas(self, _filter):
		importDAO = self.database.createImportAccessObject()
		
		try:
			datas = importDAO.getItems(_filter)
			return datas
		except:
			return Error.NETWORK