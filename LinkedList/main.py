#import the package
import LinkedList

# packagename.class
# an alternative is to use
# from LinkedList import *
# then we can use
# myList = LinkedList()
myList = LinkedList.LinkedList()

myList.append("John")
myList.append("Mafe")
myList.append("Delfi")
myList.append("Al otro")

myList.printIt()

print "length of the list ",  myList.length()