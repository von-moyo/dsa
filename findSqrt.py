def mySqrt(x: int) -> int:
    array = [2 * i + 1 for i in range(1000)]
    i = 0
    n = len(array)
    count = 0
    while i < n:
      sub = x - array[i]
      if sub >= 0:
        x = sub
        count += 1
      else:
         break
      i += 1
    return count
        
print(mySqrt(30))