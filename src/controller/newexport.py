from controller.abstractedcontroller import AbstractedViewController
from controller.error import Error

class NewExportController(AbstractedViewController):
	def __init__(self, database, exportFactory, transactionFactory, logger):
		self.database = database
		self.exportFactory = exportFactory
		self.transactionFactory = transactionFactory
		self.logger = logger

	def process(self, rawDatas, cid):
		exportDAO = self.database.createExportAccessObject()
		transactionDAO = self.database.createTransactionAccessObject()
		timestamp = self._createTimeStamp()

		# Append the BID to the list of imported items
		for data in rawDatas:
			data['CID'] = cid

		# Process the exports
		processedExports = []
		total = 0
		for data in rawDatas:
			total -= data['Qty'] * data['Price']
			processedExports.append(self.exportFactory.build(data, timestamp))

		transaction = self.transactionFactory.build({
			'CID': cid,
			'Date': timestamp,
			'Amount': total,
			'Type': 'Export'
		})


		try:
			# Push to database
			exportDAO.addItems(processedExports)
			transactionDAO.addItems([transaction])

			# Log the import
			self.logger.logCreate(processedExports)
		except:
			return Error.NETWORK

		return Error.NONE