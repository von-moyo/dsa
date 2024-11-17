from typing import List
def moveZeroes(nums: List[int]) -> None:
    noZeros = []
    zeros = []
    for num in nums:
      if num != 0:
        noZeros.append(num)
    for num in nums:
      if num == 0:
        zeros.append(num)
    return noZeros+zeros

print(moveZeroes([0,1,0,3,12]))