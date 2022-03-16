import time
import datetime

class Logger:
	def __init__(self, dao, settings, factory):
		self.user = settings.user
		self.dao = dao
		self.factory = factory

	def _createTimeStamp(self):
		return datetime.datetime.fromtimestamp(time.time(), None)

	def logCreate(self, rawDatas):
		timestamp = self._createTimeStamp()
		lst = []
		for data in rawDatas:
			log = {
				'ID': data.data['_id'],
				'User': self.user,
				'Action': 'Create',
				'Collection': data.meta.collection.name,
				'Date': timestamp
			}

			lst.append(self.factory.build(log))

		self.dao.addItems(lst)

	def logDelete(self, rawDatas):
		timestamp = self._createTimeStamp()
		lst = []

		for data in rawDatas:
			log = {
				'ID': data.data['_id'],
				'User': self.user,
				'Action': 'Delete',
				'Collection': data.meta.collection.name,
				'Date': timestamp
			}

			meta = {}
			for label in data.meta.keys:
				meta[label] = data.data[label]

			log['Meta'] = meta
			lst.append(self.factory.build(log))

		self.dao.addItems(lst)

	def logUpdate(self, rawDatas):
		timestamp = self._createTimeStamp()
		lst = []

		for data in rawDatas:
			log = {
				'ID': data['old'].data['_id'],
				'User': self.user,
				'Action': 'Modify',
				'Collection': data['new'].meta.collection.name,
				'Date': timestamp
			}

			meta = {}
			for label in data['old'].meta.keys:
				old = data['old'].data[label]
				new = data['new'].data[label]
				if old != new:
					meta[label] = {'old': old, 'new' : new}

			log['Meta'] = meta
			lst.append(self.factory.build(log))

		self.dao.addItems(lst)