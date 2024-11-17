from typing import List
def removeElement(nums: list[int], val: int) -> int:
  for i, num in enumerate(nums):
    if num == val:
      nums.pop(i)
  return len(nums), nums
print(removeElement([0,1,2,2,3,0,4,2], 2))