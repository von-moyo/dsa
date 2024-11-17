# Given the cumulative sum cs = list(accumulate(arr)), the desired partition exists if (and only if):
# cs[-1] (= sum(arr)) is divisible by three
# cs[i1] = cs[-1] // 3 for some i1
# cs[i2] = 2 * cs[-1] // 3 for some i1+1 <= i2 < len(arr) -1
# We form cs and check for the above. In the case of any error, we return False.

from itertools import accumulate
from typing import List

def canThreePartsEqualSum(arr: List[int]) -> bool:
  n = sum(arr)
  average = n//3
  count = 0
  part = 0
  remainder = n % 3
  for i in arr:
    part += i
    if part == average:
      count += 1
      part = 0
  if count == 3 and not remainder:
    return True
print(canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))