from typing import List
def findMatrix(nums: List[int]) -> List[List[int]]:
  occurrences = {}
  for item in nums:
    occurrences[item] = occurrences.get(item, 0) + 1
  results = []
  while occurrences:
    temp=[]
    erase = []
    for item, count in occurrences.items():
      temp.append(item)
      count -= 1
      occurrences[item] = count
      if count == 0:
        erase.append(item)
    results.append(temp)
    for i in erase:
      del occurrences[i]
  return results
  
print(findMatrix([1,3,4,1,2,3,1]))

# count = 0
# for i in range(1, n+1):
#   if n % i == 0:
#     count += 1
# if count == 3:
#   return True
# else:
#   return False