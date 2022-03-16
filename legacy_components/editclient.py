# from controller.abstractedcontroller import AbstractedViewController
# from controller.error import Error

# class EditSupplierController(AbstractedNewClientController):
# 	def __init__(self, database, supplierFactory, logger):
# 		self.database = database
# 		self.supplierFactory = supplierFactory
# 		self.logger = logger

# 	def process(self, rawDatas):
# 		supplierDAO = self.database.createSupplierAccessObject()

# 		updates = []
# 		for data in rawDatas:
# 			newData = self.supplierFactory.build(data['new'])

# 			if newData != data['old']:
# 				update.append({
# 					'old': data['old'],
# 					'new': newData
# 					})

# 		try:
# 			supplierDAO.setItems(update)
# 			self.logger.logUpdate(update)
# 		except:
# 			return Error.NETWORK

# 		return Error.NONE

# 	def delete(self, datas):
# 		supplierDAO = self.database.createSupplierAccessObject()

# 		try:
# 			supplierDAO.delete(datas)
# 			self.logger.logDelete(datas)
# 		except:
# 			return Error.NETWORK

# 		return Error.NONE

# class EditCustomerController(AbstractedNewClientController):
# 	def __init__(self, database, customerFactory, logger):
# 		self.database = database
# 		self.customerFactory = customerFactory
# 		self.logger = logger

# 	def process(self, rawDatas):
# 		customerDAO = self.database.createCustomerAccessObject()

# 		updates = []
# 		for data in rawDatas:
# 			newData = self.customerFactory.build(data['new'])

# 			if newData != data['old']:
# 				update.append({
# 					'old': data['old'],
# 					'new': newData
# 					})

# 		try:
# 			customerDAO.setItems(update)
# 			self.logger.logUpdate(update)
# 		except:
# 			return Error.NETWORK

# 		return Error.NONE

# 	def delete(self, datas):
# 		customerDAO = self.database.createSupplierAccessObject()

# 		try:
# 			customerDAO.delete(datas)
# 			self.logger.logDelete(datas)
# 		except:
# 			return Error.NETWORK

# 		return Error.NONE


		
