class Mobilephone:
	'Base class for all nodes'
	mobcount = 0

	def __init__(self, mobid, glat, glong):
		self.mobid = mobid
		self.glat = glat
		self.glong = glong
		Mobilephone.mobcount += 1

	def displayCount(self):
		print("Total mobilephones %d" %Mobilephone.mobcount)

	def displayMobilephone(self):
		print ("Mobid : ", self.mobid, ", Position : ", self.glat, " ", self.glong)

