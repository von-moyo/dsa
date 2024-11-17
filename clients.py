from typing import List
import heapq

def lastAssignedLocker(clients: List[str]) -> int:
    lockerMap = {}
    availableLockers = []
    lastAssignedLocker = -1
    for i in range(1, len(clients) + 1):
        heapq.heappush(availableLockers, i)
    for client in clients:
        if client in lockerMap:
            locker = lockerMap[client]
            del lockerMap[client]
            heapq.heappush(availableLockers, locker)
        else:
            locker = heapq.heappop(availableLockers)
            lockerMap[client] = locker
            lastAssignedLocker = locker  # Update last assigned locker regardless

    return lastAssignedLocker

print(lastAssignedLocker(["Alice", "Eve", "Bob", "Eve", "Carl", "Alice"]))