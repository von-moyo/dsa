from typing import List
def singleNumber(nums: List[int]):
  # Create a dictionary to count occurrences
  occurrences = {}

  # Iterate through the list and count occurrences
  for item in nums:
      occurrences[item] = occurrences.get(item, 0) + 1

  # Build a new list with only unique items
  for item, count in occurrences.items():
      if count == 1:
          return item
print(singleNumber([1,2,2,1,5]))