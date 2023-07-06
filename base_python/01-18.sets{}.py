'''
{}
sets_don't hold order and don't contain duplicate elements
'''

art_friends = {"Rolf", "Anne"}
science_friends ={"Jen", "Charlie"}

art_friends.add("Jen")

print(art_friends)

art_friends.remove("Rolf")

print(art_friends)

'''
sets_easy to compare one set to another

example: what elements are in this set that are not in this other set?
or, what elements are common between both sets?
'''