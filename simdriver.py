from mobilephone import Mobilephone
from mobilephone import Carrier
import argparse 
from time import sleep
import string, random


parser = argparse.ArgumentParser(description="Representer for the network, usage simdiver 10")
parser.add_argument("numnodes", type=int)
parser.add_argument("qoptions", type=int)
args = parser.parse_args()

nodes_list = []	
for i in nodes_list:
	del i 

def create_nodes(numnodes):
	'Create the nodes and add it into the list'


	for i in range(numnodes):
		
		# First we assign the mobid, if it already exists, we keep generating a new one until its
		# unique. This is not used currently, because in testing we can just assign them sequentially
		''' mobid = random.SystemRandom().randint(1, numnodes)
		 itemnumber = 0
		 while itemnumber < len(nodes_list):
			if (nodes_list[itemnumber].mobid == mobid):
				print "caught! " + str(nodes_list[itemnumber].mobid) + " " + str(mobid)
				mobid = random.SystemRandom().randint(1, numnodes)
				itemnumber = 0
				print "new " + str(mobid) +" resetting"
			else:
				itemnumber +=1 
		'''
		mobid = i +1		
		# At this stage (in the early version) the location attributesare not important
		glat = "glat"
		glong = "glang"
		ipaddress = "10.0.0." + (str(random.SystemRandom().randint(0, 255)))
		phone_obj = Mobilephone(mobid, glat, glong, ipaddress)
		nodes_list.append(phone_obj)
		
		#for n in nodes_list:
		#	print n.mobid
		#rand = random.SystemRandom()
		#lastOctet = str(rand.randint(0, 255))
		



def generate_question():

	q = "q1"
	n = args.qoptions
	for i in nodes_list:
		i.receive_q(q)
	return (q,n) 

def generate_responses(q, options):

	for n in nodes_list:
		n.vote(q, options)
		print "generated for "+ str(n.mobid)

def broadcast(q):

	for n in nodes_list:		# get every node to broadcast their vote
		for dest in nodes_list:	# iterate through every node to receive others' votes
			if n != dest:		# 
				print dest.vote
				n.receive(n.ipaddress, dest.ipaddress, q, dest.vote)

def get_results(q, options):
	for n in nodes_list:
		n.calculate(q, options)



if __name__ == "__main__":
	
	create_nodes(args.numnodes)

	'Print the nodes'
	for i in nodes_list:
		print "phone", i.displayMobilephone()

	print("Total number of nodes: %d" % Mobilephone.mobcount)

	carrier1 = Carrier("Telstra")
	tupq = generate_question()
	
	question =tupq[0]
	numanswers = tupq[1]
	options = int(numanswers)

	generate_responses(question, options)
	broadcast(question)	
	get_results(question, numanswers)


#	mob1.send(mob1.ipaddress, mob3.ipaddress)
#	carrier1.sendTo(mob1.ipaddress, mob3.ipaddress)
