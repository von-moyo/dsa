from typing import List
def mergeSort(nums: List[int])-> List[int]:
  n = len(nums)
  if n <= 1:
    return nums
  m = nums[n // 2]
  left = [a for a in nums if a < m]
  # print("left", left)
  middle = [a for a in nums if a == m]
  # print("middle", middle)
  right = [a for a in nums if a > m]
  # print("right", right)
  return (mergeSort(left) + middle + mergeSort(right))

print("merge sort: ")
print(mergeSort([10, 8, 21, 67, 48, 89]))

def sort(nums: List[int]) -> List[int]:
  if len(nums) <= 1:
    return nums
  n = len(nums)
  for i in range(n):
    for j in range(i + 1, n):
      if nums[i] > nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
  return nums

print("sort: ")
print(sort([1,4,2,3,8,6,5,7]))

def insertionSort(nums: List[int]) -> List[int]:
  for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > nums[i]:
      nums[j + 1] = nums[j]
      j -= 1
    nums[j + 1] = key
    
print("insertion sort: ")
print(insertionSort([1,4,2,3,8,6,5,7]))

def heapSort(nums: List[int]) -> List[int]:
  def heapify(nums, n, i):
    largest = i # largest = 0
    l = 2 * i + 1 # l = 1
    r = 2 * i + 2 # r = 2
    if l < n and nums[l] > nums[largest]: #if 1 < 5 and (nums[1] or 10) > (nums[0] or 4)
      largest = l # largest = 1
    if r < n and nums[r] > nums[largest]: #if r < 5 and (nums[2] or 3) > (nums[1] or 4)
      largest = r # largest = 2
    if largest != i: # if largest is not equal to 0
      nums[i], nums[largest] = nums[largest], nums[i] #0
      heapify(nums, n, largest)

  n = len(nums)
  for i in range(n // 2 - 1, -1, -1):
    heapify(nums, n, i)
  for i in range(n - 1, 0, -1):
    nums[i], nums[0] = nums[0], nums[i]
    heapify(nums, i, 0)
  return nums

print("heap sort: ")
print(heapSort([4, 10, 3, 5, 1]))

def quick_sort(nums: List[int]) -> List[int]:
  def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
      if nums[j] < pivot:
        i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

  def quick_sort_recursive(nums, low, high):
    if low < high:
      pi = partition(nums, low, high)
      quick_sort_recursive(nums, low, pi - 1)
      quick_sort_recursive(nums, pi + 1, high)

  quick_sort_recursive(nums, 0, len(nums) - 1)
  return nums

print("quick sort: ")
print(quick_sort([4, 10, 3, 5, 1]))