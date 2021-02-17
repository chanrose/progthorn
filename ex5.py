# Python dictionary

profile = {'Dylan': 'Has a pet hedge hog.', 'Jeff': 'Was born in Franch.', 'David': 'Can juggle.', 'Anna': 'Has arachnophobia'}

# f(x) that displaying the dictionary
def displayDict(profile):
  for key in profile:
    print(f'{key}: {profile[key]}')

print("Current profile dictionary:\n===============================")
displayDict(profile)
print('\nMaking some changes...\n===============================')
print("Changing Dylan's fact! and adding Erza profile...")

# Changing Dylan's value in the dictionary
profile['Dylan'] = 'Raise a tiger behind his home'

# Adding new key and value
profile['Ezra'] = 'Learn Taikwondo'
print("\nUpdated profile value \n===============================")
displayDict(profile)


