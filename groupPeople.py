from typing import List
def groupThePeople(groupSizes: List[int]) -> List[List[int]]:
    groups = {}
    for person, groupsize in enumerate(groupSizes):
        groups[groupsize] = groups.get(groupsize, []) + [person]
    results = []
    for key, value in groups.items():
        for i in range(0, len(value), key):
            results.append(value[i:i+key])
    return results
print(groupThePeople([3, 3, 3, 3, 3, 1, 3]))