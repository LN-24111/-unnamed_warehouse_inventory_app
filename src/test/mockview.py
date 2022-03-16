from test.mock import *
from PyQt5.QtWidgets import QApplication

qApp = QApplication([])
qApp.setStyle('Fusion')

main = type('mock', (), {})()
main.getClient = lambda :  client

vFac = createMockViewFactory(database = None, main = main)
# client = vFac.buildMainClient()
# client.show()

table = vFac.buildNewProductTable()
table.show()
