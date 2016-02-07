class Node:

	def __init__(self, val):
		self.val = val
		self.nextNode = None # Contains a reference to the next element on the list
		# If nextNode equals None, then that's the end of the list

	def printIt(self):
		print "I'm node with val = " , self.val

