class IntCheck:
	@classmethod
	def check(self, input):
# 	TODO: Refactor this shit
		# if label in ['Price', 'Quantity']:
		# 	try:
		# 		if label == 'Price':
		# 			val = float(item.text().replace(',',''))
		# 			otherCol = self.columnLabels.index('Quantity')
		# 		else:
		# 			val = int(item.text().replace(',',''))
		# 			otherCol = self.columnLabels.index('Price')
		# 		item.setBackground(Qt.white)
		# 		item.setText("{:,}".format(val))
		# 		try:
		# 			val2 = float(self.table.item(item.row(), otherCol).text().replace(',',''))
		# 			print (val2)
		# 			self.table.item(item.row(), self.columnLabels.index('Total')).setText("{:,}".format(val * val2))
		# 		except:
		# 			pass
		# 	except:
		# 		if item.text() != '':
		# 			item.setBackground(Qt.red)
		# 	finally:
		# 		total = 0
		# 		for i in range(self.table.columnCount()):
		# 			try:
		# 				total += float(self.table.item(i, self.columnLabels.index('Total')).text().replace(',',''))
		# 			except:
		# 				pass
		# 		self.billTotalAmount.setText("{:,}".format(total))
		pass

	@classmethod
	def parse(self, input):
		pass

class DateTimeCheck:
	@classmethod
	def check(self, input):
	# TODO: Refactor this shit
		# from time import strptime, strftime
		# possibleFormats = {'%Y:%m:%d', '%d:%m:%Y', '%Y/%m/%d', '%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y'}
		# f = True
		# for f in possibleFormats:
		# 	try:
		# 		date = strftime('%Y-%m-%d', strptime(item.text(), f))
		# 		f = False
		# 		item.setText(date)
		# 		break
		# 	except:
		# 		pass
		# if f:
		# 	item.setBackground(Qt.red)
		# else:
		# 	item.setBackground(Qt.white)
		pass

	@classmethod
	def parse(self, input):
		pass