from enum import Enum, auto

class Error(Enum):
	INVALID_QTY = auto()
	DUPLICATE = auto()
	NETWORK = auto()
	NONE = auto()