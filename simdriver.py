from mobilephone import Mobilephone

'Create the nodes'
mob1 = Mobilephone(1, 1, 1)
mob2 = Mobilephone(2, 2, 2)
mob3 = Mobilephone(3, 3, 3)



'Display the nodes'
mob1.displayMobilephone()
mob2.displayMobilephone()
mob3.displayMobilephone()
print("Total number of nodes: %d" % Mobilephone.mobcount)