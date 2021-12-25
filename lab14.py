#Write a Python script to check if a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def isPresent(x):
  if x in d:
      print('present')
  else:
      print('not present')
isPresent(5)
isPresent(9)
