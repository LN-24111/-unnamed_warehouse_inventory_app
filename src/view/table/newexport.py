
class ExportInflater(_Inflater):
	def __init__(self):
		super().__init__()
		self.columns = [{'title':_('ID'), 'width': 80, 'active': True, 'alignment': Qt.AlignCenter, 'parser': AllPass()},
						{'title':_('Product'), 'width': 100, 'active': False, 'alignment': Qt.AlignVCenter | Qt.AlignLeft, 'parser': AllPass()},
						{'title':_('Format'), 'width': 140, 'active': False, 'alignment': Qt.AlignVCenter | Qt.AlignLeft, 'parser': AllPass()},
						{'title':_('Unit'), 'width': 60, 'active': False, 'alignment': Qt.AlignCenter, 'parser': AllPass()},
						{'title':_('Qty'), 'width': 60, 'active': True, 'alignment': Qt.AlignCenter, 'parser': AllPass()},
						{'title':_('Price'), 'width': 90, 'active': True, 'alignment': Qt.AlignVCenter | Qt.AlignRight, 'parser': AllPass()},
						{'title':_('VAT'), 'width': 90, 'active': False, 'alignment': Qt.AlignCenter, 'parser': AllPass()},
						{'title':_('Total'), 'width': 110, 'active': False, 'alignment': Qt.AlignVCenter | Qt.AlignRight, 'parser': AllPass()},
						{'title':_('Expire'), 'width': 90, 'active': True, 'alignment': Qt.AlignCenter, 'parser': AllPass()},
						{'title':_('Manufacturer'), 'width': 100, 'active': False, 'alignment': Qt.AlignVCenter | Qt.AlignLeft, 'parser': AllPass()},
						{'title':_('Origin'), 'width': 100, 'active': False, 'alignment': Qt.AlignVCenter | Qt.AlignLeft, 'parser': AllPass()}]
		self.important = ['ID', 'Quantity', 'Price', 'Expire']