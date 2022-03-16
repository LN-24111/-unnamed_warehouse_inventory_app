import datetime
import time

# Wrapper for a data dict object
class Data:
	def __init__(self, data, meta):
		self._data = data
		self._meta = meta

	def __eq__(self, other):
		if not isinstance(other, Data):
			return False

		if type(self._meta) is not type(other._meta):
			return False

		for tag in self._meta:
			if self._data[tag] != other._data[tag]:
				return False

		return True


	@property
	def data(self):
		return self._data

	@property
	def meta(self):
		return self._meta
