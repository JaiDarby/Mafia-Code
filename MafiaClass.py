class Player:
	def __init__(self, role = 'Citizen', saved = False, dead = False):
		self.role = role
		self.saved = saved
	def is_inno(self):
		if self.role == 'Mafia':
			return False
		else:
			return True
	def can_kill(self):
		if self.role == 'Mafia':
			return True
		else:
			return False
	def can_heal(self):
		if self.role == 'Doctor':
			return True
		else:
			return False
	def can_check(self):
		if self.role == "Sheriff":
			return True
		else:
			return False