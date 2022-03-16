from random import *
from datetime import *
from time import *

def createMockSettings():
	from model.settings import Settings
	return Settings('m2root', 'LimaAlphaMike', None)

def createMockDatabase(settings = None):
	if settings is None:
		settings = createMockSettings()
	from database.mongo import MongoDatabase
	return MongoDatabase(settings)

def createMockDAOFactory(settings = None):
	from model.dao import DAOFactory
	if settings is None:
		settings = createMockSettings()
	
	database = createMockDatabase()
	database.authenticate()
	return DAOFactory(settings, database)

def createMockDataFactory():
	from model.datafactory import DataFactory
	from model.metadata import ImportMeta, ExportMeta, ClientMeta, ProductMeta, TransactionMeta, LogMeta 

	settings = createMockSettings()
	meta = None
	if type is 'Import':
		meta = ImportMeta()
	elif type is 'Export':
		meta = ExportMeta()
	elif type is 'Client':
		meta = ClientMeta()
	elif type is 'Product':
		meta = ProductMeta()
	elif type is 'Transaction':
		meta = TransactionMeta()
	elif type is 'Log':
		meta = LogMeta()
	else:
		raise Exception()

	return DataFactory(settings, meta)

def createMockLogger(settings = None, dao = None):
	from model.logger import Logger
	if dao is None:
		dao = createMockDAOFactory().createLogAccessObject()
	settings = createMockSettings()
	factory = createMockDataFactory('Log')
	return Logger(dao, settings, factory)

def createMockController(type, database = None):
	from controller.newimport import NewImportController
	from controller.newexport import NewExportController
	from controller.newdata import NewDataController

	if database is None:
		database = createMockDAOFactory()
	logger = createMockLogger(database.createLogAccessObject())

	importFactory = createMockDataFactory('Import')
	exportFactory = createMockDataFactory('Export')
	productFactory = createMockDataFactory('Product')
	clientFactory = createMockDataFactory('Client')
	transactionFactory = createMockDataFactory('Transaction')

	if type is 'NewImport':
		return NewImportController(database, importFactory, transactionFactory, logger)
	elif type is 'NewExport':
		return NewExportController(database, exportFactory, transactionFactory, logger)
	elif type is 'NewProduct':
		return NewDataController(database.createProductAccessObject(), productFactory, 'PID', logger)
	elif type is 'NewClient':
		return NewDataController(database.createClientAccessObject(), clientFactory, 'CID', logger)

def createMockViewFactory(settings = None, database = None, main = None):
	from controller.viewfactory import ViewFactory

	if settings is None:
		settings = createMockSettings()

	if database is None:
		database = createMockDatabase()

	return ViewFactory(settings, database, main)

