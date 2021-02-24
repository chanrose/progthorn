fileName = "file.txt"

i = 1
for sentence in open(fileName):
  # print(i, sentence.strip())
  print(f"{i}. {'':5} {sentence.strip()}")
  print("{}. {}".format(i, sentence.strip()))
  i += 1
 
  


  