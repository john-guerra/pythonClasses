#import the package
import LinkedList

# packagename.class
# an alternative is to use
# from LinkedList import *
# then we can use
# myList = LinkedList()
myList = LinkedList.LinkedList()

myList.add("John")
myList.add("Mafe")
myList.add("Delfi")
myList.add("Al otro")

myList.printIt()

print "length of the list ",  myList.size()