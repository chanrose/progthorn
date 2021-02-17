# Chanbroset Prach
# printing line
def printLine():
  print('────────────────────')
  
# List of students with CGPA
grades = {'Gan': 4.0, 'Dan': 4.0, 'Josept': 2.0, 'Selenium': 2.5}

printLine()
print('| {:11} {:4} |'.format("Name", "CGPA"))
printLine()

# Traversing students' grades
for (key, value) in grades.items():
  print('| {:11} {:4} |'.format(key, value))
printLine()

