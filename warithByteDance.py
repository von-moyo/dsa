# import heapq

# def calculateTikTokShoppingCost(vouchersCount, prices):
#     # Max-heap approach (negate prices to simulate max-heap using heapq)
#     max_heap = [-price for price in prices]  # Convert prices to negative to use min-heap as max-heap
#     heapq.heapify(max_heap)
    
#     # Apply vouchers
#     for _ in range(vouchersCount):
#         highest_price = -heapq.heappop(max_heap)  # Get the highest price (convert back to positive)
#         discounted_price = highest_price / 2  # Apply one voucher (halve the price)
#         heapq.heappush(max_heap, -discounted_price)  # Push the new discounted price back to the heap
    
#     # Sum up the total cost after all vouchers are applied
#     total_cost = -sum(max_heap)
#     return int(total_cost)

# # Example usage:
# vouchersCount = 3
# prices = [8, 2, 13]
# print(calculateTikTokShoppingCost(vouchersCount, prices))  # Output: 9

# import heapq

# def calculateTikTokShoppingCost(vCount, prices):
#     max_heap = [-p for p in prices]
#     heapq.heapify(max_heap)
    
#     for _ in range(vCount):
#         highest = -heapq.heappop(max_heap)
#         heapq.heappush(max_heap, -(highest / 2))
    
#     return int(-sum(max_heap))

# # Example usage:
# vCount = 3
# prices = [8, 2, 13]
# print(calculateTikTokShoppingCost(vCount, prices))  # Output: 9


def calculate_tiktok_shopping_cost(vouchers_count, prices):
    # Sort prices in descending order
    prices.sort(reverse=True)
    
    # Initialize a list to keep track of applied vouchers
    applied_vouchers = [0] * len(prices)
    
    # Apply vouchers greedily
    for _ in range(vouchers_count):
        max_savings = 0
        max_savings_index = 0
        
        # Find the item where applying a voucher saves the most money
        for i, price in enumerate(prices):
            savings = price / (2 ** (applied_vouchers[i] + 1)) - price / (2 ** applied_vouchers[i])
            if savings > max_savings:
                max_savings = savings
                max_savings_index = i
        
        # Apply the voucher to the item that saves the most
        applied_vouchers[max_savings_index] += 1
    
    # Calculate the final cost
    total_cost = sum(price / (2 ** vouchers) for price, vouchers in zip(prices, applied_vouchers))
    
    return int(total_cost)  # Return the integer part of the total cost

# Test the function with the example input
vouchers_count = 3
prices = [8, 2, 13]
result = calculate_tiktok_shopping_cost(vouchers_count, prices)
print(f"Minimum total cost: {result}")