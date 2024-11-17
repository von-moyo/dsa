# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

def addBinary(a: str, b: str):
  arrayA = [int(char) for char in a]
  n = len(arrayA)
  decA = 0
  for i in range(n):
    decA += arrayA[i] * (2 ** n)
    n -= 1
  arrayB = [int(char) for char in b]
  length = len(arrayB)
  decB = 0
  for j in range(length):
    decB += arrayB[j] * (2 ** length)
    length -= 1
  sum = decA + decB
  print("sum: ", sum)
  answer = ""
  while sum > 0:
    remainder = sum % 2
    print("remainder: ", remainder)
    answer += str(remainder)
    print("answer: ", answer)
    sum //= 2
  print(answer[::-1])

print(addBinary("1110", "1011"))