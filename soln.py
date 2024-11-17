from collections import defaultdict
from typing import List
def solution(heartRate, activityLevel):
    activity_ranges = []
    for i in range(len(activityLevel)):
        if activity_ranges and activity_ranges[-1][0] == activityLevel[i]:
            activity_ranges[-1][1].append(heartRate[i])
        else:
            activity_ranges.append([activityLevel[i], [heartRate[i]]])
    max_diff = 0
    for activity_range in activity_ranges:
        if len(activity_range[1]) > 1:
            max_diff = max(max_diff, max(activity_range[1]) - min(activity_range[1]))
    return max_diff
print(solution([60,100,90,80],["Low","High","High","High"]))
print(solution([82,120,78,61],["Normal","High","Normal","Low"]))
print(solution( [100, 87, 90, 90, 125] ,["Normal", "Normal", "Normal", "High", "Low"]))

def solution2(heartRate: List[int], activityLevel: List[str]):
    activity_ranges = defaultdict(list)
    for i in range(len(activityLevel)):
        activity_ranges[activityLevel[i]].append(heartRate[i])
    max_difference = 0
    for activity, rates in activity_ranges.items():
        if len(rates) > 1:
            max_diff = max(rates) - min(rates)
            if max_diff > max_difference:
                max_difference = max_diff
    return max_difference