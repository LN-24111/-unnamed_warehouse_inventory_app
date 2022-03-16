from controller.abstractedcontroller import AbstractedViewController
from controller.error import Error

class NewImportController(AbstractedViewController):
	def __init__(self, database, importFactory, transactionFactory, logger):
		self.database = database
		self.importFactory = importFactory
		self.transactionFactory = transactionFactory
		self.logger = logger

	def process(self, rawDatas, sid):
		importDAO = self.database.createImportAccessObject()
		transactionDAO = self.database.createTransactionAccessObject()
		timestamp = self._createTimeStamp()

		# Append the SID to the list of imported items
		for data in rawDatas:
			data['SID'] = sid

		# Process the imports
		processedImports = []
		total = 0
		for data in rawDatas:
			total += data['Qty'] * data['Price']
			processedImports.append(self.importFactory.build(data, timestamp))

		transaction = self.transactionFactory.build({
			'CID': sid,
			'Date': timestamp,
			'Amount': total,
			'Type': 'Import'
		})

		try:
			# Push to database
			importDAO.addItems(processedImports)
			transactionDAO.addItems([transaction])

			# Log the import
			self.logger.logCreate(processedImports)
		except:
			return Error.NETWORK

		return Error.NONE