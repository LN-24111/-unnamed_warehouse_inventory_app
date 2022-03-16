from controller.abstractedcontroller import AbstractedViewController
from controller.error import Error

class NewDataController(AbstractedViewController):
	def __init__(self, dao, factory, uid, logger):
		self.dao = dao
		self.factory = factory
		self.uid = uid
		self.logger = logger

	def process(self, rawDatas):
		error = self.checkDuplicateNewDatas(dao, rawDatas, uid)
		if error is not Error.NONE:
			return error

		newDatas = []
		for data in rawDatas:
			item = self.factory.build(data)
			newDatas.append(item)

		try:
			self.dao.addItems(newDatas)
			self.logger.logCreate(newDatas)
		except:
			return Error.NETWORK

		return Error.NONE
