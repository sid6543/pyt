a = set()

a.add(1)
a.add(2)
a.add(2)
a.add(3)
a.add(1)
a.add(3)

a.add((4,5,6)) #You can add tuple in a set.
# a.add([7,8,9]) #You can not add list in the set.
# a.add({10:11}) #You can not add dictionary in the set.
print(a)