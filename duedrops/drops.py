#DueDrop's event object
class Drop:
	def __init__(self, name, entrydate, duedate, reminder):
		self.name = name
		self.entrydate = entrydate
		self.duedate = duedate
		self.reminder = reminder
		self.dismissed = False
		if reminder == 0:
			self.dismissed = True

#DueDrop's overall calendar object
class Faucet:
	def __init__(self, drops, owner, ownermail)
		self.drops = drops # list of Drops
		self.owner = owner
		self.ownermail = ownermail
