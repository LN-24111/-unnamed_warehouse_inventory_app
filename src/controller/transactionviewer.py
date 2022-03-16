from controller.error import Error

class TransactionViewer:
	def __init__(self, database):
		self.dao = database.createTransactionAccessObject()

	def getDatas(self, _filter):
		try:
			datas = self.dao.getItems(_filter)
			return datas
		except:
			return Error.NETWORK