from test.mock import *
from test.dbControl import *
from test.mockdata import *

iCtrl = createMockController('NewImport')
eCtrl = createMockController('NewExport')
cCtrl = createMockController('NewClient')
tCtrl = createMockController('NewTransaction')

def testICtrl():
	iCtrl.process(imData[0:10], 'TSLR')

def testECtrl():
	exports = []
	for i in items:
		ID = i.data['ID']
		export = {
			'ID': i.data['ID'],
			'Qty': i.data['Qty'] - randrange(5),
			'Price': randrange(2000) * 1000,
			'Expire': i.data['Expire']
		}
		exports.append(export)

	eCtrl.process(exports, 'TBR')
