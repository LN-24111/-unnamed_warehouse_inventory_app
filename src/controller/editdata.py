from controller.abstractedcontroller import AbstractedViewController
from controller.error import Error

class EditDataController(AbstractedViewController):
	def __init__(self, dao, factory, logger):
		self.dao = dao
		self.factory = factory
		self.logger = logger

	def process(self, rawDatas):
		updates = []
		for data in rawDatas:
			newData = self.factory.build(data['new'])

			if newData != data['old']:
				update.append({
					'old': data['old'],
					'new': newData
					})
		try:
			self.dao.setItems(update)
			self.logger.logUpdate(update)
		except:
			return Error.NETWORK

		return Error.NONE

	def delete(self, datas):
		try:
			self.dao.delete(datas)
			self.logger.logDelete(datas)
		except:
			return Error.NETWORK

		return Error.NONE

	def getDatas(self, _filter):
		try:
			datas = self.dao.getItems(_filter)
			return datas
		except:
			return Error.NETWORK