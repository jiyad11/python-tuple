# x = ('orange','apple','kiwi')
# y = list(x)
# y[1]=('banana')
# x=tuple(y)
# print(x)  #tuple is unchangable, but we can change tuple by converting it into list then convert back to tuple

# thistuple=('orange','apple')
# x = list(thistuple)
# x.append('banana')
# thistuple= tuple(x)
# print(thistuple) #append item by convert in into list

# thistuple=('orange','apple','banana')
# newtuple=('mango',)
# thistuple+=newtuple
# print(thistuple) #add 2 tuples

# thistuple = ('apple','mango','banana')
# thislist = list(thistuple)
# thislist.remove('mango')
# thistuple=tuple(thislist)
# print(thistuple) #remove items in tuple by convert it into list then remove then convert back into tuple

thistuple = ('apple','mango','banana')
del thistuple #tuple deleted entirely
