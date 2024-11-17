from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
  nums.sort()
  result = []
  n = len(nums)
  for i in range(n):
    if i > 0 and nums[i] == nums[i - 1]:
      continue
    left, right = i + 1, n - 1
    while left < right:
      total = nums[i] + nums[left] + nums[right]
      if total == 0:
        result.append([nums[i], nums[left], nums[right]])
        while left < right and nums[left] == nums[left + 1]:
          left += 1
        while left < right and nums[right] == nums[right - 1]:
          right -= 1
        left += 1
        right -= 1
      elif total < 0:
        left += 1
      else:
        right -= 1
  return result

# Test the function
print(threeSum([-1, 0, 1, 2, -1, -4]))

# def three_sum(nums):
#     print(f"Initial array: {nums}") 
#     nums.sort()
#     print(f"Sorted array: {nums}")
    
#     result = []
#     print("Starting the main loop...\n")
    
#     for i in range(len(nums) - 2):
#         print(f"Index i: {i}, nums[i]: {nums[i]}")
        
#         if i > 0 and nums[i] == nums[i - 1]:
#             print(f"Skipping duplicate for nums[i]: {nums[i]}")
#             continue
        
#         left, right = i + 1, len(nums) - 1
#         print(f"Initial left pointer: {left}, nums[left]: {nums[left]}")
#         print(f"Initial right pointer: {right}, nums[right]: {nums[right]}")
        
#         while left < right:
#             total = nums[i] + nums[left] + nums[right]
#             print(f"Checking triplet: {nums[i]}, {nums[left]}, {nums[right]} -> Sum: {total}")
            
#             if total == 0:
#                 print(f"Found a triplet: {nums[i]}, {nums[left]}, {nums[right]}")
#                 result.append([nums[i], nums[left], nums[right]])
                
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#                     print(f"Skipping duplicate at left, new left: {left}, nums[left]: {nums[left]}")
                
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
#                     print(f"Skipping duplicate at right, new right: {right}, nums[right]: {nums[right]}")
                
#                 left += 1
#                 right -= 1
#                 print(f"Moving pointers -> New left: {left}, New right: {right}")
#             elif total < 0:
#                 left += 1
#                 print(f"Total < 0, moving left pointer to: {left}")
#             else:
#                 right -= 1
#                 print(f"Total > 0, moving right pointer to: {right}")
        
#         print("\n" + "-" * 40 + "\n")
    
#     print(f"Final result: {result}")
#     return result

# nums = [-1, 0, 1, 2, -1, -4]
# three_sum(nums)
