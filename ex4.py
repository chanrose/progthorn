# Chanbroset Prach

groceries = []
while True:
  item = input("Enter an item (<ENTER> when done): ")
  # Checking input if anything written
  if len(item):
    # Adding the item to the groceries
    groceries.append(item)
    print("Item added.")
  else:
    break

print("\nHere is your shopping list:")
for item in groceries:
  # Convert index into string and showing the item
  print(str(groceries.index(item)+1) + ". " + item)
