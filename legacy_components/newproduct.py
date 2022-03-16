# from controller.abstractedcontroller import AbstractedViewController
# from controller.error import Error

# class NewProductController(AbstractedNewClientController):
# 	def __init__(self, database, productFactory, logger):
# 		self.database =database
# 		self.productFactory = productFactory
# 		self.logger = logger

# 	def process(self, rawDatas):
# 		productDAO = self.database.createProductAccessObject()

# 		error = self.checkDuplicateNewDatas(productDAO, rawDatas, 'ID')
# 		if error is not Error.NONE:
# 			return error

# 		newProducts = []
# 		for data in rawDatas:
# 			product = self.productFactory.build(data)
# 			newProducts.append(product)

# 		try:
# 			productDAO.addItems(newProducts)
# 			self.logger.logCreate(newProducts)
# 		except:
# 			return Error.NETWORK

# 		return Error.NONE
