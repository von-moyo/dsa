from typing import List
def majorityElement(nums: List[int]) -> int:
  n = len(nums)
  count = {}
  for item in nums:
    count[item] = count.get(item, 0) + 1
  for key, value in count.items():
    if value > n // 2:
      return key
print(majorityElement([2,2,1,1,1,2,2]))