from pymongo import MongoClient
from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal
from database.collections import Collection
# This database class is implemented on CLIENT side. It does not have a dedicated server handler (as it should be)
# As a result, security is limited, and the logging system is there to provide info and protect against user mistakes
class MongoDatabase:

	def __init__(self, settings):
		self.settings = settings

	def authenticate(self):
		query = self.settings.query
		self._client = MongoClient(query, w=2, wtimeout=1000)
		try:
			# This will throw an error if auth is bad. Can't find a proper 'auth' method that returns a boolean
			self._client.server_info()

			# cache data declaration
			self.db = self._client.pharmacy
			self.collections = {
				Collection.PRODUCT : self.db.product,
				Collection.CLIENT : self.db.client_,
				Collection.IMPORT : self.db.import_,
				Collection.EXPORT : self.db.export,
				Collection.TRANSACTION : self.db.transaction,
				Collection.LOG : self.db.log
			}
		except:
			raise Exception('Cannot connect to database, query: {}'.format(query))

	def _getItems(self, cursor):
		lst = []
		for i in range(cursor.count()):
			lst.append(cursor.next())

		return lst

	def getItems(self, collectionEnum, _filter = None):
		collection = self.collections[collectionEnum]
		cursor = collection.find(_filter)
		return self._getItems(cursor)
		
	def getItemsByDate(self, collectionEnum, begin, end):
		collection = self.collections[collectionEnum]
		cursor = collection.find({'Date' : {'$gte': begin, '$lte' : end}})
		return self._getItems(cursor)

	def addItems(self, collectionEnum, items):
		collection = self.collections[collectionEnum]
		lst = [item.data for item in items]
		collection.insert_many(lst)

	def setItems(self, collectionEnum, items):
		collection = self.collections[collectionEnum]
		for item in items:
			collection.replace_one(item['old'].data, item['new'].data)

	def deleteItems(self, collectionEnum, items):
		collection = self.collections[collectionEnum]
		lst = [item.data for item in items]
		collection.delete_many({'$or': lst})

	def close(self):
		self._client.close()