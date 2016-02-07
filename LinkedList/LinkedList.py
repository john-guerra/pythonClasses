# Homework, create the class LinkedList that has four methods, a constructor, append, printIt and length
from Node import *


class LinkedList:
	def __init__(self):
		self.head = None

	def add(self, val):

		tempNode = Node(val)

		if (self.head == None):
			self.head = tempNode

		tail = getTail()
		if (tail):
			tail.nextNode = tempNode


	# Returns the current tail of the list
	def getTail(self):

	def size(self):
		pass



	# iterates over the whole list printing each node
	def printIt(self):

		node = self.head

		while node != None:
			node.printIt()
			node = node.nextNode
