from controller.error import Error

class SalesTracker:
	def __init__(self, database):
		self.database = database

	def getDatas(self, _filter):
		exportDAO = database.createExportAccessObject()
		productDAO = database.createProductAccessObject()

		try:
			exports = exportDAO.getItems(_filter)
			PIDs = []
			sales = []
		
			for entry in exports:
				for item in sales:
					if entry.data['PID'] is item['PID']:
						item['Sales'].append({
							'Date': entry.data['Date'],
							'Qty': entry.data['Qty']
						})
				else:
					item = {
						'PID': entry.data['PID'],
						'Sales': {
							'Date': entry.data['Date'],
							'Qty': entry.data['Qty']
						}
					}
					sales.append(item)

					PIDs.append({
						'PID': entry.data['PID']
					})

			products = productDAO.getItems({'$or': PIDs})

			return sales, products
		except:
			return Error.NETWORK