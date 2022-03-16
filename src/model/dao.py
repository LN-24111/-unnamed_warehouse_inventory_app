from model.datafactory import DataFactory
from model.metadata import *
from database.collections import Collection

class DAOFactory:
	def __init__(self, settings, database):
		self.database = database
		self.settings = settings

	def createProductAccessObject(self):
		return DataAccess(self.database, Collection.PRODUCT, DataFactory(self.settings, ProductMeta()))

	def createImportAccessObject(self):
		return DataAccess(self.database, Collection.IMPORT, DataFactory(self.settings, ImportMeta()))

	def createClientAccessObject(self):
		return DataAccess(self.database, Collection.CLIENT, DataFactory(self.settings, ImportMeta()))

	def createExportAccessObject(self):
		return DataAccess(self.database, Collection.EXPORT, DataFactory(self.settings, ExportMeta()))

	def createTransactionAccessObject(self):
		return DataAccess(self.database, Collection.TRANSACTION, DataFactory(self.settings, TransactionMeta()))

	def createLogAccessObject(self):
		return DataAccess(self.database, Collection.LOG, DataFactory(self.settings, TransactionMeta()))

	# def createSupplierAccessObject(self):
	# 	return DataAccess(self.database, Collection.SUPPLIER, DataFactory(self.settings, SupplierMeta()))

	# def createCustomerAccessObject(self):
	# 	return DataAccess(self.database, Collection.CUSTOMER, DataFactory(self.settings, CustomerMeta()))

	# def createInventoryAccessObject(self):
	# 	return DataAccess(self.database, Collection.INVENTORY, DataFactory(self.settings, InventoryMeta()))

class DataAccess:
	def __init__(self, database, collection, factory):
		self._database = database
		self._collection = collection
		self._factory = factory

	@property
	def collection(self):
		return self._collection
	
	def getItemsByDate(self, begin, end):
		items = self._database.getItemsByDate(self._collection, begin, end)
		return [self._factory.build(item) for item in items]

	def getItems(self, _filter = None):
		items = self._database.getItems(self._collection, _filter)
		return [self._factory.build(item) for item in items]

	def setItems(self, items):
		if (len(items) == 0):
			return
		self._database.setItems(self._collection, items)

	def addItems(self, items):
		if (len(items) == 0):
			return
		self._database.addItems(self._collection, items)

	def deleteItems(self, items):
		if (len(items) == 0):
			return
		self._database.deleteItems(self._collection, items)