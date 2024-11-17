from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  """
  Do not return anything, modify nums1 in-place instead.
  """
  nums1 = [num for num in nums1 if num != 0]
  array = (nums1 + nums2)
  array.sort()
  for i in range(m + n):
    nums1[i] = array[i]

  sliced = nums1[0: m]
  array = sliced + nums2
  array.sort()
  nums1 = array
  print(nums1)

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))