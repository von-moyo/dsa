from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    for i in nums:
        if nums[i] == target:
            return i
        else:
            return 5678
# print(searchInsert([1,3,5,6], 5))


def search(nums: List[int], target: int) -> int:
    for i, value in enumerate(nums):
        if value == target:
            return i
# print(search([1,3,5,6], 5))


def binarySearch(array: List[int], target: int) -> int:
  n = len(array)
  lower = 0
  upper = n - 1

  while lower <= upper: #while 5 <= 7... while 5 <= 5...
    mid = (lower + upper) // 2 #4 #5
    if target == array[mid]: #array[mid] = 8 so if 9 == 8... no. so if 9 == 9... yes
      return mid #return 5
    elif target < array[mid]: # if 9 < 8... no if 9 < 12... yes upper = 5
      upper = mid - 1
    elif target > array[mid]: # if 9 > 9 then lower = 5
      lower = mid + 1
  return -1
print(binarySearch([1, 3, 5, 6, 8, 9, 12, 67], 9))