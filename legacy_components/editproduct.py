# from controller.abstractedcontroller import AbstractedViewController
# from controller.error import Error

# class EditProductController(AbstractedNewClientController):
# 	def __init__(self, database, productFactory, logger):
# 		self.database = database
# 		self.productFactory = productFactory
# 		self.logger = logger

# 	def process(self, rawDatas):
# 		productDAO = self.database.createProductAccessObject()

# 		updates = []
# 		for data in rawDatas:
# 			newData = self.productFactory.build(data['new'])

# 			if newData != data['old']:
# 				update.append({
# 					'old': data['old'],
# 					'new': newData
# 					})
# 		try:
# 			productDAO.setItems(update)
# 			self.logger.logUpdate(update)
# 		except:
# 			return Error.NETWORK

# 		return Error.NONE

# 	def delete(self, datas):
# 		productDAO = self.database.createProductAccessObject()

# 		try:
# 			productDAO.delete(datas)
# 			self.logger.logDelete(datas)
# 		except:
# 			return Error.NETWORK

# 		return Error.NONE
