# Code
# Testcase
# Test Result
# Test Result
# 2652. Sum Multiples
# Easy
# Topics
# Companies
# Hint
# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

# Return an integer denoting the sum of all numbers in the given range satisfying the constraint.


# Example 1:

# Input: n = 7
# Output: 21
# Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.

def sumOfMultiples(n: int) -> int:
  count = 0
  for i in range(1, n+1):
    if i%3 == 0 or i%5 == 0 or i%7 == 0:
      count +=i
  return count

print(sumOfMultiples(10))