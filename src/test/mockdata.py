from random import *
from datetime import *
from time import *

imData = []
clData = []
prData = []

for i in range (1000):
	randomImport = {
		'ID': i,
		'Qty': randrange(1000),
		'Price': randrange(1000) * 1000,
		'Expire': datetime(2020,1,1),
		'SID': i
		}
	imData.append(randomImport)

	randomClient = {
		'SID': i,
		'Name': 'Jane Doe',
		'Address': 'Unknown',
		'TIN': None
	}
	clData.append(randomClient)

	randomProduct = {
		'ID': i,
		'Name': 'MS' + str(randrange(1000)),
		'Format': 'Bottle' if randrange(2) is 0 else 'Tube',
		'Unit': 'Box' if randrange(2) is 0 else 'Pill',
		'Manufacturer': 'TST',
		'Origin': 'UK' if randrange(2) is 0 else 'USA'
		}
	prData.append(randomProduct)