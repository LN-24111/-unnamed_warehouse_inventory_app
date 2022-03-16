# from controller.abstractedcontroller import AbstractedViewController
# from controller.error import Error

# class NewSupplierController(AbstractedNewClientController):
# 	def __init__(self, database, supplierFactory, logger):
# 		self.database = database
# 		self.supplierFactory = supplierFactory
# 		self.logger = logger

# 	def process(self, rawDatas):
# 		supplierDAO = self.database.createSupplierAccessObject()

# 		# Verify no duplicate. This is VERY problematic if concurrent is a thing... but it's not
# 		# Webserver required for concurrent access
# 		error = self.checkDuplicateNewDatas(supplierDAO, rawDatas, 'SID')
# 		if error is not Error.NONE:
# 			return error

# 		newSuppliers = []
# 		for data in rawDatas:
# 			supplier = self.supplierFactory.build(data)
# 			newSuppliers.append(supplier)

# 		try:
# 			supplierDAO.addItems(newSuppliers)
# 			self.logger.logCreate(newSuppliers)
# 		except:
# 			return Error.NETWORK

# 		return Error.NONE

# class NewCustomerController(AbstractedNewClientController):
# 	def __init__(self, database, customerFactory, logger):
# 		self.database = database
# 		self.customerFactory = customerFactory
# 		self.logger = logger

# 	def process(self, rawDatas):
# 		customerDAO = self.database.createCustomerAccessObject()

# 		error = self.checkDuplicateNewDatas(customerDAO, rawDatas, 'CID')
# 		if error is not Error.NONE:
# 			return error

# 		newCustomers = []
# 		for data in rawDatas:
# 			customer = self.customerFactory.build(data)
# 			newCustomers.append(customer)

# 		try:
# 			customerDAO.addItems(newCustomers)
# 			self.logger.logCreate(newCustomers)
# 		except:
# 			return Error.NETWORK

# 		return Error.NONE
