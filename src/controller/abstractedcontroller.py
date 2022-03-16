import time
import datetime
from controller.error import *

# General controller methods
class AbstractedViewController:
	def getProducts(self, _filter = None):
		self.database.createProductAccessObject().getItems(_filter)

	def getCustomers(self, _filter = None):
		self.database.createCustomerAccessObject().getItems(_filter)

	def getSuppliers(self, _filter = None):
		self.database.createSupplierAccessObject().getItems(_filter)

	def _createTimeStamp(self):
		return datetime.datetime.fromtimestamp(time.time(), None)

	def checkDuplicatesNewDatas(self, dao, rawDatas, uid):
		try:
			idList = [{uid: data[uid]} fromtimestampr data in rawDatas]
			duplicates = dao.getItems({'$or': idList})

			if duplicates or len(idList) != len(set(idList)):
				return Error.DUPLICATE
		except:
			return Error.NETWORK

		return Error.NONE


	# def _findInventory(self, datas):
	# 	inventoryDAO = self.database.createInventoryAccessObject()
	# 	fltr = [{'ID': data['ID'],'Expire': data['Expire']} for data in datas]

	# 	return inventoryDAO.getItems({'$or': fltr})

	# This function returns a modified inventory based on import/export data without doing actual database
	# 
	# def _modifyInventory(self, rawDatas, export=False):
	# 	currentInventory = self._findInventory(rawDatas)
	# 	updatedInventory = []
	# 	newInventory = []

	# 	for data in rawDatas:
	# 		for inventory in currentInventory:
	# 			if inventory.data['ID'] == data['ID'] and inventory.data['Expire'] == data['Expire']:
	# 				if export:
	# 					# Not enough for export
	# 					if inventory.data['Qty'] < data['Qty']:
	# 						return Error.INVALID_QTY

	# 					inventory = self.inventoryFactory.build({
	# 						'ID': data['ID'],
	# 						'Qty': inventory.data['Qty'] - data['Qty'],
	# 						'Expire': data['Expire']
	# 						})
	# 					updatedInventory.append(inventory)

	# 				else:
	# 					inventory = self.inventoryFactory.build({
	# 						'ID': data['ID'],
	# 						'Qty': inventory.data['Qty'] + data['Qty'],
	# 						'Expire': data['Expire']
	# 						})
	# 					updatedInventory.append(inventory)

	# 				break
	# 		else:
	# 			if export:
	# 				return Error.INVALID_QTY
	# 			else:
	# 				inventory = self.inventoryFactory.build({
	# 					'ID': data['ID'],
	# 					'Qty': data['Qty'],
	# 					'Expire': data['Expire']
	# 					})
	# 				newInventory.append(inventory)

	# 	update = [{'old': currentInventory[i], 'new': updatedInventory[i]} for i in range(len(currentInventory))]
		
	# 	if export:
	# 		return update
	# 	else:
	# 		return (update, newInventory)