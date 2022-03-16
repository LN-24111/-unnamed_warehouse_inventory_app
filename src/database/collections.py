from enum import Enum, auto

class Collection(Enum):
	PRODUCT = auto()
	CLIENT = auto()
	IMPORT = auto()
	EXPORT = auto()
	TRANSACTION = auto()
	LOG = auto()
	# INVENTORY = auto()