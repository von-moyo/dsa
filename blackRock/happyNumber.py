import sys

def is_happy_number(n):
  seen = set()
  while n != 1 and n not in seen:
      seen.add(n)
      n = sum(int(digit) ** 2 for digit in str(n))
  return n == 1

for line in sys.stdin:
  n = int(line.strip())
  if is_happy_number(n):
      print(1)
  else:
      print(0)