class ClientInflater(_Inflater):
	def __init__(self):
		super().__init__()
		self.columns = [{'title': _('PID'), 'width': 120, 'active': True, 'alignment': Qt.AlignCenter, 'parser': AllPass()},
						{'title':_('Name'), 'width': 210, 'active': True, 'alignment': Qt.AlignVCenter | Qt.AlignLeft, 'parser': AllPass()},
						{'title':_('Address'), 'width': 320, 'active': True, 'alignment': Qt.AlignVCenter | Qt.AlignLeft, 'parser': AllPass()},
						{'title':_('TIN'), 'width': 100, 'active': True, 'alignment': Qt.AlignCenter, 'parser': AllPass()}]
		self.important = ['ID', 'Name']

