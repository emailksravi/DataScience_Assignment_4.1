"""
Problem Statement​ ​2:
Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
"""

class list_Utilities:
 def __init__(self, wordlist):
  self.wordlist = wordlist
  print ("Initialised list_Utilities object")

 def filter_long_words(self, n):
  return list(filter(lambda x:len(x) > n, self.wordlist))

instance = list_Utilities(["This","is","a","beautiful","day"])
print ("New List of Words  => " + str(instance.filter_long_words(3)) ) 
 
