def anagrams(word1: str, word2: str) -> bool:
  word1 = word1.lower().replace(" ", "")
  word2 = word2.lower().replace(" ", "")
  if len(word1) != len(word2):
    return False
  count1 = {}
  count2 = {}
  for item in word1:
    count1[item] = count1.get(item, 0) + 1
  for item in word2:
    count2[item] = count2.get(item, 0) + 1
  print(count1)
  print(count2)
  return count1 == count2
print(anagrams("cheetar", "teacher"))

def anagrams2(word1: str, word2: str) -> bool:
  word1 = word1.lower().replace(" ", "")
  word2 = word2.lower().replace(" ", "")
  if len(word1) != len(word2):
    return False
  arrayOfword1Count = [0] * 26
  arrayOfword2Count = [0] * 26

  for char in word1:
    index = ord(char) - ord('a')
    arrayOfword1Count[index] += 1

  for char in word2:
    index = ord(char) - ord('a')
    arrayOfword2Count[index] += 1
  return arrayOfword1Count == arrayOfword2Count

print(anagrams2("cheetar", "teacher"))

def anagrams3(word1: str, word2: str) -> bool:
  sortedWord1 = sorted(word1)
  sortedWord2 = sorted(word2)
  return sortedWord1 == sortedWord2
print(anagrams3("cheetar", "teacher"))

from collections import Counter
def anagrams4(word1: str, word2: str) -> bool:
  counter1 = Counter(word1)
  counter2 = Counter(word2)
  print(counter1)
  return counter1 == counter2
print(anagrams4("cheetar", "teacher"))