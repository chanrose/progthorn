# Fill in the blank game 
# Chanbroset Prach

def character_detail():
  print("Creating character....\n==================================\n")
  noun = input("Name: ")
  verb = input("Hobby: ")
  adjective = input("Appearance: ")
  return [noun.strip(), verb.lower().strip(), adjective.strip()]

def print_story(character = []): 
  if len(character):
    noun, verb, adjective = character 
  else:
    noun = verb = adjective = "[_______]"

  print("\n==================================\n")
  print(f"Just below the police station, there is a morgue where the forensic dissecting the corpse of the victim to find out the cause and time of death. {noun}, {adjective}, is a new officier in the station. He is {verb} just right behind his house. While the new officier {noun} is {verb}, just few meters away, a man suddenly collapse and die on spot. {noun} checked the pulse and declared him death. Unclear by the death method, {noun} called the forensics who working at the morgue to help check the cause of death ")

print("Fill in the blank")
print_story()
print_story(character_detail())

