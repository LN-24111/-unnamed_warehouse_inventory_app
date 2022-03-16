from controller.error import Error

class InventoryViewer:
	def __init__(self, database):
		self.database = database

	def getDatas(self, _filter):
		importDAO = database.createImportAccessObject()
		exportDAO = database.createExportAccessObject()
		productDAO = database.createProductAccessObject()

		try:
			imports = importDAO.getItems(_filter)
			exports = exportDAO.getItems(_filter)
			PIDs = []
			inventory = []

			# Calculate current inventory
			for entry in imports:
				for item in inventory:
					if entry.data['PID'] is item['PID'] and entry.data['Expire'] == item['Expire']:
						item['Qty'] += entry.data['Qty']
				else:
					item = {
						'PID': entry.data['PID'],
						'Qty': entry.data['Qty'],
						'Expire': entry.data['Expire']
					}
					inventory.append(item)
					PIDs.append({
						'PID': entry.data['PID']
					})

			for entry in exports:
				for item in inventory:
					if entry.data['PID'] is item['PID'] and entry.data['Expire'] == item['Expire']:
						item['Qty'] -= entry.data['Qty']
				else:
					item = {
						'PID': entry.data['PID'],
						'Qty': -entry.data['Qty'],
						'Expire': entry.data['Expire']
					}
					inventory.append(item)
					PIDs.append({
						'PID': entry.data['PID']
					})

			products = productDAO.getItems({'$or': PIDs})

			return inventory, products
		except:
			return Error.NETWORK