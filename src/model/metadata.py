from database.collections import Collection
def _(message) : return message

class Meta:
	@property
	def collection(self):
		return self._collection

	@property
	def keys(self):
		return self._keys.copy()

	@property
	def important(self):
		return self._important.copy()
	
class ClientMeta(Meta):
	def __init__(self):
		self._keys = ['CID','Name', 'Address', 'TIN']
		self._important = ['CID', 'Name', 'Address']
		self._collection = Collection.CLIENT

class ProductMeta(Meta):
	def __init__(self):
		self._keys = ['PID', 'Name', 'Format', 'Unit', 'VAT', 'Manufacturer', 'Origin']
		self._important = ['PID', 'Name', 'Format', 'Unit']
		self._collection = Collection.PRODUCT

class TransactionMeta(Meta):
	def __init__(self):
		self._keys = ['CID', 'Date', 'Amount', 'Type']
		self._important = ['CID', 'Date', 'Amount']
		self._collection = Collection.TRANSACTION

class ImportMeta(Meta):
	def __init__(self):
		self._keys = ['PID', 'Qty', 'Price', 'Expire', 'SID', 'Date']
		self._important = ['PID', 'Qty', 'Price', 'Expire', 'SID', 'Date']
		self._collection = Collection.IMPORT

class ExportMeta(Meta):
	def __init__(self):
		self._keys = ['PID', 'Qty', 'Price', 'Expire', 'CID', 'Date']
		self._important = ['PID', 'Qty', 'Price', 'Expire', 'CID', 'Date']
		self._collection = Collection.EXPORT

class LogMeta(Meta):
	def __init__(self):
		self._keys = ['ID', 'User', 'Action', 'Collection', 'Date', 'Meta']
		self._important = ['ID', 'User', 'Action', 'Collection', 'Date', 'Meta']
		self._collection = Collection.LOG

# class CustomerMeta(Meta):
# 	def __init__(self):
# 		self._keys = ['CID','Name', 'Address', 'TIN']
# 		self._important = ['CID', 'Name', 'Address']
# 		self._collection = Collection.CUSTOMER

# class SupplierMeta(Meta):
# 	def __init__(self):
# 		self._keys = ['SID','Name', 'Address', 'TIN']
# 		self._important = ['SID', 'Name', 'Address']
# 		self._collection = Collection.SUPPLIER

# class InventoryMeta(Meta):
# 	def __init__(self):
# 		self._keys = ['PID', 'Qty', 'Expire']
# 		self._important = ['PID', 'Qty', 'Expire']
# 		self._collection = Collection.INVENTORY