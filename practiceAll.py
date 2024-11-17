from typing import List
def twoSum(array: List[int], target)-> int:
  n = len(array)
  for i in range(n):
    remainder = target - array[i]
    for j in range(i+1, n):
      if array[j] == remainder:
        return [i,j]
print(twoSum([2,7,11,9,15,6], 22))
