# thistuple = ('apple','mango','banana')
# (red,green,yellow)=thistuple
# print(red)
# print(green)
# print(yellow) #unpack tuple


# thistuple = ('apple','mango','banana','kiwi') #Using Asterisk* :
# (red,*green)=thistuple #If the number of variables is less than the number of values,
# print(red) #you can add an * to the variable name
# print(green) #and the values will be assigned to the variable as a list (here into list green).

thistuple = ('apple','mango','banana','papaya','kiwi')
(red,*yellow,green)=thistuple
print(red) #If the asterisk* is added to another variable name than the last,
print(yellow) # Python will assign values to the variable until the number of values left matches
print(green) # the number of variables left.