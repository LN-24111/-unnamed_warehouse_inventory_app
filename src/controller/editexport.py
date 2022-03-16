from controller.abstractedcontroller import AbstractedViewController
from controller.error import Error

class EditExportController(AbstractedViewController):
	def __init__(self, database, exportFactory, transactionFactory, logger):
		self.database = database
		self.exportFactory = exportFactory
		self.transactionFactory = transactionFactory
		self.logger = logger

	def process(self, rawDatas, sid):
		exportDAO = self.database.createExportAccessObject()
		transactionDAO = self.database.createTransactionAccessObject()

		# Update the export database
		update = []
		for data in rawDatas:
			timestamp = data['old'].data['Date']

			newData = self.exportFactory.build(data['new'], timestamp)

			if newData != data['old']:
				update.append({
					'old': data['old'],
					'new': newData
					})

			total-= data['new']['Qty'] * data['new']['Price']

		# Update the transaction database
		newTransaction = self.transactionFactory.build({
			'CID': sid,
			'Date': timestamp,
			'Amount': total,
			'Type': 'Export'
		})

		oldTransaction = transactionDAO.getItems({
			'Date': timestamp,
			'Type': 'Export'
		})[0]

		updateTransaction = {
			'old': oldTransaction,
			'new': newTransaction
		}

		try:
			exportDAO.setItems(update)
			transactionDAO.setItems(updateTransaction)

			self.logger.logUpdate(update)
		except:
			return Error.NETWORK

		return Error.NONE

	def delete(self, datas):
		exportDAO = self.database.createExportAccessObject()

		try:
			exportDAO.delete(datas)
			self.logger.logDelete(datas)
		except:
			return Error.NETWORK

		return Error.NONE

	def getDatas(self, _filter):
		exportDAO = self.database.createExportAccessObject()
		
		try:
			datas = exportDAO.getItems(_filter)
			return datas
		except:
			return Error.NETWORK