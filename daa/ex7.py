# Chanbroset Prach 
# Set exercise

line = '\n────────────────────────────────────────────────────────────────────────────────────\n'
D1 = {'Bob', 'Tom', 'Peter', 'Laura', 'Dan', 'Mary', 'Timmy'}
D2 = {'Kim', 'Tom', 'Neil', 'Kramer', 'Dan', 'Jimmy', 'Teresa'}

# Print Sets
print("Set 1:", line, D1)
print("\nSet 2:", line, D2)

# Common members between both
print("\nCommon members: ", line, D1 & D2)

# Members that are either in each but not both
print("\nMembers that are in D1 or D2 but not both:", line, (D1 ^ D2))

# Unique members only in D1
print("\nUnique members in D1", line, D1 - D2)


print("\nList of all members with no duplicate",line, ((D1 | D2) - (D1 & D2)))

print("\nList of both sets enabled duplicate record:", line, list(D1 | D2) + list(D1 & D2))

