import os, random

class Mobilephone:
	'Base class for all nodes'
	mobcount = 0
	hash

	def __init__(self, mobid, glat, glong, ipaddress):
		self.mobid = mobid
		self.glat = glat
		self.glong = glong
		self.ipaddress = ipaddress

		Mobilephone.mobcount += 1

	def displayCount(self):
		print("Total mobilephones %d" %Mobilephone.mobcount)

	def displayMobilephone(self):
		print ("Mobid : ", self.mobid, ", IP: ", self.ipaddress,  ", Position : ", \
																	 self.glat, " ", self.glong)

	def send(self, ipsrc, ipdest, message):
		print ("sending to %s", ipdest)


	def receive(self, ipsrc, ipdest, q, message):
		print ("receiving from %s %s", ipsrc, message)
		nodepath = "testdata" + "/" + str(self.mobid)
		filename = q + ".txt"
		if not os.path.exists(nodepath):
			pass 	#os.makedirs(nodepath) 	
		else:
			with open(os.path.join(nodepath,filename), "a") as file:
				file.write(message)	#appends every option it receives from other nodes
									# if I'm not interested in this q for now, should I still receive everyone's votes?
									# if I do, then that is a lot more traffic, but if I don't and I decide to contribute at the end
									# then I will just need to rely on existing data being passed by other nodes


	def receive_q(self, question):
		nodepath = "testdata" + "/" + str(self.mobid)
		print ("New question %d", self.mobid)
		if not os.path.exists(nodepath):
			os.makedirs(nodepath)

		filename = question + ".txt"
		with open(os.path.join(nodepath,filename), "w") as file:
			pass
	
	def vote(self, question, numanswers):
		vote = str(random.SystemRandom().randint(1, numanswers))
		nodepath = "testdata" + "/" + str(self.mobid)
		filename = question + ".txt"
		if not os.path.exists(nodepath):
			os.makedirs(nodepath)

		with open(os.path.join(nodepath,filename), "w") as file:
			file.write(vote)
		self.vote = vote	

	def calculate(self, question, numanswers):
		nodepath = "testdata" + "/" + str(self.mobid)
		filename = question + ".txt"
		if os.path.exists(nodepath):
			with open(os.path.join(nodepath,filename)) as file:
				lines = file.readlines()
				results = {}
				print ("lines", lines)
				for char in lines[0]: 
					print ("char", char)
					print results
					if char in results:
						results[char] += 1
						print str(char) + "inc here"
					else:
						results[char] = 1
						print str(char) + "new here"
			# now print results
			for key, count in results.iteritems():
				print "Key, count", key, count




class Carrier:
	'Base class for all connecting carriers'

	def __init__(self, bizname):
		self.bizname = bizname
		dict = {'user1': '10.0.0.2', 'user2': '10.0.0.3', 'user3': '10.0.0.4'}

	def sendTo(self, ipsrc, ipdest):
		print ("Carrier sending to %d", ipdest)




	def find(self, ipdest):
		pass


'''
Public methods:
	- sendTo

Internal methods:
	- findIP


'''

