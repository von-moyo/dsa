from typing import List
def garbageCollection(garbage: List[str], travel: List[int]) -> int:
  glass = 0
  metal = 0
  paper = 0
  n = len(garbage)
  m = False
  p = False
  g = False
  for i in range(n-1,-1,-1):
    if not g and "G" in garbage[i]:
      g = True
      glass+=sum(travel[:i])
      print(travel[:i])
    if not m and "M" in garbage[i]:
      m = True
      metal+=sum(travel[:i])
      print(travel[:i])
    print("glass: ", metal)
    if not p and "P" in garbage[i]:
      p = True
      paper+=sum(travel[:i])
      print(travel[:i])
    if all([m,p,g]):
      break
  print("glass: ", glass)
  print("paper: ", paper)
  print(len("".join(garbage)))
  print("".join(garbage))
  return len("".join(garbage))+glass+metal+paper
print(garbageCollection(["G","P","GP","GG"], [2,4,3]))