# Homework, create the class LinkedList that has four methods, a constructor, append, printIt and length
from Node import *


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, val):

		tempNode = Node(val)

		if (self.head == None):
			self.head = tempNode

		# Updates the nextNode link of the previous tail
		if (self.tail != None):
			self.tail.nextNode = tempNode

		self.tail = tempNode




	def size(self):
		pass

	def printIt(self):
		pass