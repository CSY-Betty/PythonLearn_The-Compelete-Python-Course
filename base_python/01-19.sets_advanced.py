art_friends = {"Rolf", "Anne","Jen"}
science_friends ={"Jen", "Charlie"}

'''
art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)
=>

symmetric_difference - not_in_both

doesn't matter which one goes first
art_friends.symmetric_difference(science_friends) = science_friends.symmetric_difference(art_friends)

intersection - both

union - all
unite both sets to become one big set and duplicate one is gonna appear once in the final set
'''
not_in_both = art_friends.symmetric_difference(science_friends)

print(not_in_both)

art_and_science = art_friends.intersection(science_friends)

print(art_and_science)

all_friends = art_friends.union(science_friends)

print(all_friends)