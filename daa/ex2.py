# Ask user how far they wish to travel (in km)

dist = float(input("Distance (km): "))

if dist < 5:
  print("Let's save the planet by walking there instead")
elif dist < 500:
  print("That's kind of far, let's drive")
else:
  print("It's better to just fly")