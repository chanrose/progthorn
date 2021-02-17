# Chanbroset Prach 
# Set exercise
def printLine():
  print('\n──────────────────────────────────────────────────────────────────────────────────────────────────────\n')
  

D1 = {'Bob', 'Tom', 'Peter', 'Laura', 'Dan', 'Mary', 'Timmy'}
D2 = {'Kim', 'Tom', 'Neil', 'Kramer', 'Dan', 'Jimmy', 'Teresa'}

# Combined set
D3 = D1.union(D2)

printLine()
# Print Sets
print("Set 1:", D1)
print("Set 2:", D2)

# Common members between both
printLine()
com_set = [ele for ele in D1 if ele in D2]
print("Common members: ", com_set)
printLine()

# Members that are either in each but not both
print("Members that are in D1 or D2 but not both:\n" + str([ele for ele in D3 if ele not in com_set]))
printLine()

# Unique members only in D1
print("Unique members in D1\n" + str([ele for ele in D1 if ele not in D2]))
printLine()

print("List of all members from both D1 and D2\n" + str([ele for ele in D3]))
printLine()


# I'm not sure about list down all the members in D1 and D2, does it mean allow duplication?