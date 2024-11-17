# from collections import Counter

# def countMinimumCharactersForVideoIDs(idStream, videoIds):
#     result = []
#     for target in videoIds:
#         target_count = Counter(target)
#         current_count = Counter()
#         found = False
#         for i, char in enumerate(idStream):
#             current_count[char] += 1
#             if all(current_count[c] >= target_count[c] for c in target_count):
#                 result.append(i + 1)
#                 found = True
#                 break
#         if not found:
#             result.append(-1)
#     return result

# # Example usage
# idStream = "064819848398"
# videoIds = ["088", "364", "07"]
# output = countMinimumCharactersForVideoIDs(idStream, videoIds)
# print(output)  # Expected output: [7, 10, -1]

def countMinimumCharactersForVideolDs(idStream, videoIds):
    n = len(idStream)
    m = len(videoIds)
    counts = [[0] * (n + 1) for _ in range(10)]

    # Precompute cumulative counts
    for i in range(n):
        digit = int(idStream[i])
        for d in range(10):
            counts[d][i + 1] = counts[d][i]
        counts[digit][i + 1] += 1

    result = []
    for videoId in videoIds:
        required_counts = [0] * 10
        for ch in videoId:
            required_counts[int(ch)] += 1

        low, high = 1, n + 1  # Initialize binary search bounds
        ans = -1
        while low < high:
            mid = (low + high) // 2
            satisfied = True
            for d in range(10):
                if counts[d][mid] < required_counts[d]:
                    satisfied = False
                    break
            if satisfied:
                high = mid
            else:
                low = mid + 1
        if low <= n:
            ans = low
        else:
            ans = -1
        result.append(ans)
    return result

# Example usage:
idStream = "064819848398"
videoIds = ["088", "364", "07"]
print(countMinimumCharactersForVideolDs(idStream, videoIds))  # Output: [7, 10, -1]