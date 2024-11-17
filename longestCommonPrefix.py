from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
  prefix = ""
  i = 0
  n = len(strs)
  if n == 0:
    return prefix
  while i < len(strs[0]):
    char = strs[0][i]
    for j in range(1, n):
      if strs[j][i] != char:
        return prefix
    prefix += char
    i += 1
  return prefix
print(longestCommonPrefix(["flower","flow","flight"]))