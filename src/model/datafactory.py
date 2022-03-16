import time
import datetime
from model.data import Data

class DataFactory:
	'''Create specific Data instances'''
	def __init__(self, settings, meta):
		'''
		settings: configurations
		meta: meta data used to make objects
		'''
		self._settings = settings
		self._meta = meta

	def _sanitize(self, rawData, timeStamp):
		data = {}
		for key in self._meta.keys:
			if key in rawData:
				data[key] = rawData[key]
			else:
				if key == 'Date':
					data[key] = timeStamp
				else:
					data[key] = ''

		return data

	def build(self, rawData, timeStamp = None):
		data = self._sanitize(rawData, timeStamp)

		if '_id' in rawData:
			data['_id'] = rawData['_id']

		return Data(data, self._meta)

