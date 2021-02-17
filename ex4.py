# Chanbroset Prach

groceries = []
while True:
  item = input("Enter an item (<ENTER> when done): ")
  if len(item):
    groceries.append(item)
    print("Item added.")
  else:
    break

print("\nHere is your shopping list:")
for item in groceries:
  print(str(groceries.index(item)+1) + ". " + item)
