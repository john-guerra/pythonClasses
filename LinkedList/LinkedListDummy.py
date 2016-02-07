# Homework, create the class LinkedList that has four methods, a constructor, append, printIt and length

class LinkedList:
	def __init__(self):
		self._innerList = []


	def add(self, val):
		self._innerList.append(val)
		return True


	def size(self):
		return len(self._innerList)

	def printIt(self):
		for ele in self._innerList:
			print ele