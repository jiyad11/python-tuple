# thistuple=("muhammed","jiyad",10,12.80)
# print(thistuple) #use ordinary bracket

# thistuple=("muhammed","jiyad",10,"muhammed","jiyad")
# print(thistuple) #allow duplicates

# thistuple=('muhammed','jiyad',10)
# print(len(thistuple)) #to determine how many items a tuple has, use len() function

# thistuple=('muhammed',) #To create a tuple with only one item,
# print(type(thistuple)) #you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# thistuple=('muhammed')
# print(type(thistuple)) #see, python not recognising this as a tuple instead its recongnized as string.

thistuple= tuple(('muhammed','jiyad'))
print(thistuple) #construct tuple