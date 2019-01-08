__author__ = 'Dhruv Panchal'

"""Think of at least five places in the world you would like to visit. 
   Store the locations in a list. Make sure the list is not in alphabetical order."""

places=['new york', 'florida', 'arizona', 'nevada', 'california']

#Print your list in its original order.
print ("Original List : ", places)

#Use sorted() to print your list in alphabetical order without modifying the actual list.
print ("Sorted List : ", sorted(places))

#Show that your list is still in its original order by printing it.
print ("Original List : ", places)

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print ("Reverse Sorted List :  ", sorted(places,reverse=True))

#Show that your list is still in its original order by printing it again.
print("Original List : ", places)

#Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print ("Reverse List : ", places)

#Use reverse() to change the order of your list again. Print the list to show it is back to its original order.
places.reverse()
print ("Reverse List : ", places)

#Use sort() to change your list so it is stored in alphabetical order. Print the list to show that its order has been changed.
places.sort()
print ("Sort List : ", places)

#Use sort() to change your list so it is stored in reverse alphabetical order. Print the list to show that its order has changed.
places.sort(reverse=True)
print ("Reverse Sort List : ", places)

#Get length of your list.
print ("Length of the list is : ",len(places))
