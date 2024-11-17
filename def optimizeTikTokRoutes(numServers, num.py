def optimizeTikTokRoutes(numServers, numDisconnectedPairs, disconnectedPairs):
    disconnected = [[False] * (numServers + 1) for _ in range(numServers + 1)]
    
    for a, b in disconnectedPairs:
        disconnected[a][b] = True
        disconnected[b][a] = True

    goodSubsegments = 0

    for start in range(1, numServers + 1):
        for end in range(start, numServers + 1):
            isGood = True
            for i in range(start, end + 1):
                for j in range(i + 1, end + 1):
                    if disconnected[i][j]:
                        isGood = False
                        break
                if not isGood:
                    break
            if isGood:
                goodSubsegments += 1

    return goodSubsegments

# Example usage:
numServers = 4
numDisconnectedPairs = 2
disconnectedPairs = [
    [1, 2],
    [2, 3]
]

print(optimizeTikTokRoutes(numServers, numDisconnectedPairs, disconnectedPairs))  # Output: 8
