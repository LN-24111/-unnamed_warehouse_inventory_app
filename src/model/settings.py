import toml

class Settings:
	__config = None
	__values = {
	# App config
		'general_language'		: 'en',
		'import_UseCalendar'	: True,
		'import_IDNew'			: True,
		'import_IDFind'			: False,
		'import_ClientNew'		: False,
		'import_ClientFind'		: False,
		'export_IDFind'			: True,
	# Database config
		'database_query'		: 'mongodb+srv://{0}:{1}@testdb-bla2l.mongodb.net/test?retryWrites=true'
	}

	# Other informations
	__user = None
	
	# Global states
	def __init__(self, username, password, main, config = 'config.toml'):
		self.__config = config
		try:
			data = toml.load(self.__config)
			for key, value in self.__values.items():
				self.__values[key] = data[key] if data.get(key) != None else value
		except:
			pass

		self.__main = main
		self.__user = username
		self.query = self.__values['database_query'].format(username, password)
		self.__save()

	@property
	def values(self):
		return self.__values.copy()

	@values.setter
	def values(self, data):
		for key, value in self.__values.items():
			self.__values[key] = data[key] if data.get(key) != None else value

		self.__save()

	def __save(self):
		with open(self.__config, 'w') as f:
			toml.dump(self.__values, f)

	@property
	def user(self):
		return self.__user