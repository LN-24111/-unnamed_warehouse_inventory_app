from test.mock import *

DAOFactory = createMockDAOFactory()
DAOImport = DAOFactory.createImportAccessObject()
DAOExport = DAOFactory.createExportAccessObject()
DAOClient = DAOFactory.createClientAccessObject()
DAOProduct = DAOFactory.createProductAccessObject()
DAOTransaction = DAOFactory.createTransactionAccessObject()
DAOLog = DAOFactory.createLogAccessObject()

def clearAll():
	clear(DAOImport)
	clear(DAOExport)
	clear(DAOClient)
	clear(DAOProduct)
	clear(DAOTransaction)
	clear(DAOLog)

def clear(dao):
	items = dao.getItems()
	if len(items) > 0:
		dao.deleteItems(items)