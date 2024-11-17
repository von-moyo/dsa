from typing import List
def finalPrices(prices: List[int]) -> List[int]:
  discount = []
  for i in range(len(prices)):
    amount = 0
    for j in range(i+1, len(prices)):
      if prices[j] <= prices[i]:
        amount  = prices[j]
        break
    discount.append(prices[i] - amount)
  return discount

print(finalPrices([8, 4, 6, 2, 3]))
# expected output is [4,2,4,2,3]